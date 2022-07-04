from dataclasses import dataclass
from typing import ClassVar, Union

from src.domain.building.exceptions import InvalidUnityName, UnityNameAlreadyRegistered
from src.domain.building.value_object import ApartmentUnities, ComercialUnities


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
    _TYPE: ClassVar[ApartmentUnities] = ApartmentUnities


class ComercialUnity(BaseUnity):
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


@dataclass
class Unity:
    _registered: ClassVar[set] = set()

    expenses: PayableExpenses
    reference: Union[ApartmentUnity, ComercialUnity]

    def __post_init__(self):
        if self.reference.name in self._registered:
            raise UnityNameAlreadyRegistered(f"{self.reference.name} is already registered")

        self._registered.add(self.reference.name)

    @property
    def name(self):
        return self.reference.name
