from django.db import models
from django.db.models import F, Q, Func

class DeasManager(models.Manager):
    def with_distance(self, latitude, longitude):
        """
        Returns a QuerySet of locations annotated with their distance from the
        given point. This can then be filtered.
        Usage:
            Foo.objects.within(lat, lon).filter(distance__lt=10).count()
        
        Extracted from the following stackoverflow answer:
        @see http://stackoverflow.com/a/31715920/1373318
        """
        class Sin(Func):
            function = 'SIN'
        class Cos(Func):
            function = 'COS'
        class Acos(Func):
            function = 'ACOS'
        class Radians(Func):
            function = 'RADIANS'

        radlat = Radians(latitude) # given latitude
        radlong = Radians(longitude) # given longitude
        radflat = Radians(F('lat'))
        radflong = Radians(F('long'))

        # Using Haversine formula
        # Note 3959.0 is for miles. Use 6371 for kilometers
        Expression = 6371 * Acos(Cos(radlat) * Cos(radflat) *
                                   Cos(radflong - radlong) +
                                   Sin(radlat) * Sin(radflat))

        return self.get_queryset()\
            .exclude(lat=None)\
            .exclude(long=None)\
            .annotate(distance=Expression)

    def order_by_locality(self):
        return self.get_queryset()\
            .exclude(Q(locality__exact=""))\
            .order_by("locality")

    def order_by_postal_code(self):
        return self.get_queryset()\
            .exclude(Q(postal_code__exact=""))\
            .order_by("postal_code")

    def search_by_locality(self, locality):
        return self.get_queryset().filter(Q(locality__icontains=locality))

    def search_by_postal_code(self, postal_code):
        return self.get_queryset().filter(Q(postal_code__icontains=postal_code))

    def search_by_company_ownership(self):
        return self.get_queryset().filter(Q(ownership__icontains='Privada'))

class DjangoDea(models.Model):

    class Meta:
        db_table = "devices"

    id = models.UUIDField(primary_key=True)
    locality = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    device_location = models.CharField(max_length=300, blank=True, null=True)
    postal_code = models.CharField(max_length=5)
    lat = models.IntegerField()
    long = models.IntegerField()
    ownership = models.CharField(max_length=20)

    objects = DeasManager()