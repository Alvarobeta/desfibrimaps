from abc import ABC, abstractmethod
from typing import Optional, List

""" from thelibrary_core.context.library.domain.address import AddressId, Address
from thelibrary_core.context.library.domain.location import LocationId
from thelibrary_core.context.library.domain.door import DoorId """


class BookRepository(ABC):

    @abstractmethod
    def find_one_by_id(self, address_id: AddressId) -> Optional[Address]:
        pass

    @abstractmethod
    def find_by_door_ids(self, door_id_list: List[DoorId]) -> List[Address]:
        pass

    @abstractmethod
    def get_by_id(self, address_id: AddressId) -> Optional[Address]:
        pass

    @abstractmethod
    def count_by_location_id_and_main_entrance(self, location_id: LocationId) -> int:
        pass

    @abstractmethod
    def create_addresses(self, addresses: List[Address]) -> List[Address]:
        pass

    @abstractmethod
    def update(self, address: Address):
        pass

