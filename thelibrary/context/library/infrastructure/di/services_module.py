from injector import Module, singleton, provider

from citibox_core.context.expansion.domain.address import AddressRepository, NormalizedAddressRepository
from citibox_core.context.expansion.domain.address.location_addresses_builder import LocationAddressesBuilder
from citibox_core.context.expansion.domain.door import DoorRepository
from citibox_core.context.expansion.domain.device import DeviceRepository
from citibox_core.context.expansion.domain.box.box_builder import BoxBuilder
from citibox_core.context.expansion.domain.box.box_repository import BoxRepository
from citibox_core.context.expansion.domain.company import CompanyRepository
from citibox_core.context.expansion.domain.contact.contact_repository import ContactRepository
from citibox_core.context.expansion.domain.location import LocationRepository, LocalityRepository, RegionRepository, \
    LocationBuilder
from citibox_core.context.expansion.domain.installation_task.installation_task_repository import InstallationTaskRepository
from citibox_core.context.expansion.infrastructure.django.repositories import LocationRepositoryDjango, \
    LocalityRepositoryDjango, RegionRepositoryDjango, NormalizedAddressRepositoryDjango, CompanyRepositoryDjango, \
    AddressRepositoryDjango, DoorRepositoryDjango, DeviceRepositoryDjango
from citibox_core.context.expansion.infrastructure.django.repositories.box_repository_django import BoxRepositoryDjango

from citibox_core.context.expansion.infrastructure.django.repositories.contact_repository_django import \
    ContactRepositoryDjango
from citibox_core.context.expansion.infrastructure.django.repositories.installation_task_repository_django import \
    InstallationTaskRepositoryDjango


class ServicesModule(Module):

    def configure(self, binder):
        binder.bind(LocationRepository, to=LocationRepositoryDjango(), scope=singleton)
        binder.bind(LocalityRepository, to=LocalityRepositoryDjango(), scope=singleton)
        binder.bind(RegionRepository, to=RegionRepositoryDjango(), scope=singleton)
        binder.bind(CompanyRepository, to=CompanyRepositoryDjango(), scope=singleton)
        binder.bind(InstallationTaskRepository, to=InstallationTaskRepositoryDjango(), scope=singleton)
        binder.bind(AddressRepository, to=AddressRepositoryDjango(), scope=singleton)
        binder.bind(NormalizedAddressRepository, to=NormalizedAddressRepositoryDjango(), scope=singleton)
        binder.bind(BoxRepository, to=BoxRepositoryDjango(), scope=singleton)
        binder.bind(ContactRepository, to=ContactRepositoryDjango(), scope=singleton)
        binder.bind(DoorRepository, to=DoorRepositoryDjango(), scope=singleton)
        binder.bind(DeviceRepository, to=DeviceRepositoryDjango(), scope=singleton)

    @provider
    @singleton
    def provide_incident_service(
        self,
        location_repository: LocationRepository,
        locality_repository: LocalityRepository,
        region_repository: RegionRepository,
        company_repository: CompanyRepository,
        contact_repository: ContactRepository
    ) -> LocationBuilder:
        return LocationBuilder(
            location_repository=location_repository,
            locality_repository=locality_repository,
            region_repository=region_repository,
            company_repository=company_repository,
            contact_repository=contact_repository
        )

    @provider
    @singleton
    def provide_box_service(
        self,
        location_repository: LocationRepository,
        box_repository: BoxRepository
    ) -> BoxBuilder:
        return BoxBuilder(
            location_repository=location_repository,
            box_repository=box_repository
        )

    @provider
    @singleton
    def provide_location_addresses_service(
        self,
        address_repository: AddressRepository
    ) -> LocationAddressesBuilder:

        return LocationAddressesBuilder(address_repository=address_repository)
