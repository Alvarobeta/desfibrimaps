import uuid

from typing import Optional, List, Set

from thelibrary_core.context.library.domain.book import BookRepository
""" from citibox_core.context.shared.infrastructure.django.models import LocationAddress, CountryAddressType, \
    LocationAddressesDoor
from citibox_core.context.expansion.domain.address import AddressId, Address, AddressRepository
from citibox_core.context.expansion.domain.address.exceptions import LocationAddressDoesNotExistException
from citibox_core.context.expansion.domain.location import LocationId
from citibox_core.context.expansion.domain.door import DoorId """


class BookRepositoryDjango(BookRepository):

    """ def find_one_by_id(self, address_id: AddressId) -> Optional[Address]:
        address = LocationAddress.objects.filter(pk=address_id).first()
        return address.to_expansion_domain_model() if address else None

    def find_by_door_ids(self, door_id_list: List[DoorId]) -> List[Address]:
        # Distinct because there are cases in which a door can exist in many Addresses and we need to avoid
        # return an address twice
        addresses_qs = LocationAddress.objects.filter(location_address_doors__door_id__in=door_id_list).distinct()
        return [address.to_expansion_domain_model() for address in addresses_qs]

    def count_by_location_id_and_main_entrance(self, location_id: LocationId) -> int:
        counter = 0
        # todo this could be done with a manager that traduces main_entrance=true to order=1
        # and main_entrance=False to order=2. Currently we can not filter by main_entrance because it's a property.
        previous_addresses = LocationAddress.objects.filter(location_id=location_id)
        for previous_address in previous_addresses:
            if previous_address.main_entrance:
                counter += 1

        return counter

    def get_by_id(self, address_id: AddressId) -> Address:
        try:
            address = LocationAddress.objects.get(id=address_id)
        except LocationAddress.DoesNotExist:
            raise LocationAddressDoesNotExistException()

        return address.to_expansion_domain_model()

    def create_addresses(self, addresses: List[Address]) -> List[Address]:
        address_types = {address.address_type for address in addresses}
        address_type_mapper = self._get_address_type_mapper(address_types, addresses[0].country.value)

        location_id = addresses[0].location_id
        previous_addresses = set(LocationAddress.objects.filter(location_id=location_id))

        infra_addresses = [
            LocationAddress(
                lat=address.coordinates.latitude,
                lon=address.coordinates.longitude,
                location_id=address.location_id,
                main_entrance=address.main_entrance,
                type=address_type_mapper.get(address.address_type),
                name=address.name,
                number=address.number,
                additional_information=address.additional_information,
                postal_code=address.postal_code
            ) for address in addresses
        ]
        LocationAddress.objects.bulk_create(infra_addresses)
        after_addresses = LocationAddress.objects.filter(location_id=location_id)

        new_addresses = set(after_addresses) - previous_addresses

        return [address.to_expansion_domain_model() for address in new_addresses]

    def update(self, address: Address) -> None:
        if address.is_deleted():
            self._delete_address(address)

        else:
            address_type_mapper = self._get_address_type_mapper({address.address_type}, address.country.value)

            LocationAddress.objects.filter(id=address.id).update(
                lat=address.coordinates.latitude,
                lon=address.coordinates.longitude,
                location_id=address.location_id,
                order=1 if address.main_entrance else 2,
                type=address_type_mapper.get(address.address_type),
                name=address.name,
                number=address.number,
                additional_information=address.additional_information,
                postal_code=address.postal_code
            )

    @staticmethod
    def _delete_address(address: Address):
        # todo descomentar cuando se quiera eliminar de verdad la location_address, quitar el pass
        LocationAddressesDoor.objects.filter(location_address_id=address.id).delete()
        LocationAddress.objects.filter(id=address.id).delete()

    @staticmethod
    def _get_address_type_mapper(address_type_names: Set[str], country_id) -> List[CountryAddressType]:
        address_types = CountryAddressType.objects.filter(name__in=address_type_names)
        missing_address_types = address_type_names - {address_type.name for address_type in address_types}

        if missing_address_types:
            new_address_types = [
                CountryAddressType(id=uuid.uuid4(), name=address_type, country_id=country_id)
                for address_type in missing_address_types
            ]
            CountryAddressType.objects.bulk_create(new_address_types)

            address_types = CountryAddressType.objects.filter(name__in=address_type_names)

        return {address_type.name: address_type for address_type in address_types}
 """