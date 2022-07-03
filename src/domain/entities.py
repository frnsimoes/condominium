from dataclasses import dataclass
from typing import ClassVar, Union

from src.domain._types import Apartment, Comercial, UnityType, get_unity_possible_values
from src.domain import apartment_string_id, comercial_string_id

Reference = Union[Apartment, Comercial]


@dataclass
class PayableExpenses:
    water: bool = True
    energy: bool = False
    fire_energy: bool = True
    internet: bool = False
    cleaner: bool = True
    apartments_utilitaries: bool = False
    generic_utilitaries: bool = True


@dataclass
class Unity:
    _registered: ClassVar[set] = set()

    type: UnityType
    expenses: PayableExpenses
    reference: Reference

    def __post_init__(self):
        if self.reference not in get_unity_possible_values():
            raise Exception("reference is not a possible value")

        if self.reference in self._registered:
            raise Exception("reference already registered")

        if self.type not in UnityType.values():
            raise Exception("Type must be Apartment or Comercial")

        self._registered.add(self.reference)

    def count_registered_unities(self):
        return len(self._registered)

    def count_registered_apartment_unities(self):
        return len([e.startswith(apartment_string_id) for e in self._registered])

    def count_registered_comercial_unities(self):
        return len([e.startswith(comercial_string_id) for e in self._registered])
