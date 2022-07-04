from enum import Enum, auto, unique


class BaseEnum(Enum):
    def _generate_next_value_(name: str, start, count, last_values):
        return name

    @classmethod
    def values(cls):
        return [e.value for e in cls]


class BaseUnities(BaseEnum):
    def _generate_next_value_(name: str, start, count, last_values):
        name = name.replace("_", ".")
        if name.startswith("CO_"):
            name = name.replace("CO", "S")

        return name


@unique
class UnityTypes(BaseEnum):
    APARTMENT = auto()
    COMERCIAL = auto()


@unique
class ApartmentUnities(BaseUnities):
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
class ComercialUnities(BaseUnities):
    CO_01 = auto()
    CO_02 = auto()
    CO_03 = auto()
    CO_04 = auto()
