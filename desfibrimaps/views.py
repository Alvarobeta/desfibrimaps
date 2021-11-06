from django.views import generic
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .infrastructure.django.models import DjangoDea
from .forms import DeaForm
from .forms import NearestDeaForm
from django.db.models import Q, F
import math

class DeaDetailView(generic.DetailView):
    model = DjangoDea
    template_name = 'dea.html'


class OrderByLocality(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'deas_list'
    paginate_by = 20

    def get_queryset(self):
        return DjangoDea.objects.order_by_locality()


class OrderByPostalCode(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'deas_list'
    paginate_by = 20

    def get_queryset(self):
        return DjangoDea.objects.order_by_postal_code()


def index(request):
    locality = request.GET.get('search_dea_by_locality')
    postal_code = request.GET.get('search_dea_by_postal_code')
    company_ownership = request.GET.get('search_dea_by_company')
    
    deas = DjangoDea.objects.all()

    if locality:
        deas = DjangoDea.objects.search_by_locality(locality)
    if postal_code:
        deas = DjangoDea.objects.search_by_postal_code(postal_code)
    if company_ownership:
        deas = DjangoDea.objects.search_by_company_ownership()

    paginator = Paginator(deas, 20) # Show 20 DEAs per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj})


def create(request):
    if request.method == 'POST':
        form = DeaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeaForm()

    return render(request, 'create.html', {'form': form})


def nearest(request):
# Coordinades for check
# Lat     Long
# 4476960 439237 
# 4474120 440921
# 4495388 404248
    if request.method == 'POST':
        form = NearestDeaForm(request.POST)

        if form.is_valid():
            lat = float(request.POST.get("lat"))
            lon = float(request.POST.get("long"))             
            distance = 1 # distance in km

            queryset = DjangoDea.objects\
                .with_distance(lat, lon)\
                .filter(distance__lt=distance)\
                .order_by("distance")[0:1]

            return render(request, 'nearest.html', {'deas': queryset,'form': form})
    else:
        form = NearestDeaForm()
        
    return render(request, 'nearest.html', {'form': form})