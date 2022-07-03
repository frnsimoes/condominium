from dataclasses import dataclass
from typing import ClassVar, Union

from src.constants import Apartment, Comercial, Type, get_unity_possible_values

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

    type: Type
    expenses: PayableExpenses
    reference: Reference

    def __post_init__(self):
        if self.reference not in get_unity_possible_values():
            raise Exception("reference is not a possible value")

        if self.reference in self._registered:
            raise Exception("reference already registered")

        self._registered.add(self.reference)
