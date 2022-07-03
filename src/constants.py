from enum import Enum, auto, unique


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        if "_" in name:
            return name.replace("_", ". ")
        return name

    @classmethod
    def values(cls):
        return [e.value for e in cls]


@unique
class Type(AutoName):
    APARTMENT = auto()
    COMERCIAL = auto()


@unique
class Apartment(AutoName):
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
class Comercial(AutoName):
    S_01 = auto()
    S_02 = auto()
    S_03 = auto()
    S_04 = auto()


def get_unity_possible_values() -> list:
    return Apartment.values() + Comercial.values()
