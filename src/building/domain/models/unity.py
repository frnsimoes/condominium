from dataclasses import dataclass
from typing import ClassVar, Set, Union

from src.building.domain.exceptions import (
    InvalidUnityName,
    UnityAlreadyRegistered,
    UnityNameAlreadyRegistered,
)
from src.building.domain.value_object import ApartmentUnities, ComercialUnities


class BaseUnity:
    _TYPE: ClassVar[Union[ApartmentUnities, ComercialUnities]] = None

    def __init__(self, name):
        assert self._TYPE is not None, "class variable _TYPE must be implemented"
        self.name = name
        if self.name not in self._TYPE.values():
            raise InvalidUnityName(f"{self.name} is not a possible value for {self._TYPE.__name__}")

    @classmethod
    def available_unities(cls) -> int:
        return len(cls._TYPE.values())

    @classmethod
    def string_id(cls) -> str:
        return cls._TYPE.__name__[:2].upper()


class ApartmentUnity(BaseUnity):
    GAS = True
    _TYPE: ClassVar[ApartmentUnities] = ApartmentUnities


class ComercialUnity(BaseUnity):
    GAS = False
    _TYPE: ClassVar[ComercialUnities] = ComercialUnities


@dataclass(frozen=True)
class PayableExpenses:
    water: bool = True
    energy: bool = False
    fire_energy: bool = True
    internet: bool = False
    cleaner: bool = True
    apartments_utilitaries: bool = False
    generic_utilitaries: bool = True


@dataclass(unsafe_hash=True)
class Unity:
    registered_refs: ClassVar[Set[str]] = set()
    registered_unities: ClassVar[list] = list()

    expenses: PayableExpenses
    reference: Union[ApartmentUnity, ComercialUnity]

    def __post_init__(self):
        if self.reference.name in self.registered_refs:
            raise UnityNameAlreadyRegistered(f"{self.reference.name} is already registered")
        self.registered_refs.add(self.reference.name)

        self.registered_unities.append(self)

    @property
    def name(self):
        return self.reference.name

    @classmethod
    def get_payers_per_expense(cls, expense_name: str):
        return [unity for unity in cls.registered_unities if getattr(unity.expenses, expense_name)]
