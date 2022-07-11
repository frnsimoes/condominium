from enum import Enum, auto, unique
from typing import Any, List


class BaseEnum(Enum):
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: List[Any]) -> Any:

        return name

    @classmethod
    def values(cls) -> List[str]:
        return [e.value for e in cls]


class BaseUnities(BaseEnum):
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: List[Any]) -> Any:

        name = name.replace("_", ".")
        if name.startswith("CO_"):
            name = name.replace("CO", "S")

        return name


@unique
class UnityTypes(BaseEnum):
    APARTMENT = auto()
    COMERCIAL = auto()


@unique
class Apartment(BaseUnities):
    AP_01 = auto()
    AP_02 = auto()
    AP_03 = auto()
    AP_04 = auto()
    AP_05 = auto()
    AP_06 = auto()
    AP_07 = auto()
    AP_08 = auto()
    AP_09 = auto()
    AP_10 = auto()
    AP_11 = auto()
    AP_12 = auto()


@unique
class Comercial(BaseUnities):
    CO_01 = auto()
    CO_02 = auto()
    CO_03 = auto()
    CO_04 = auto()
