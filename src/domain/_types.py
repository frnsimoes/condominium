from enum import Enum, auto, unique


class BaseEnum(Enum):
    def _generate_next_value_(name: str, start, count, last_values):
        return name

    @classmethod
    def values(cls):
        return [e.value for e in cls]


class Reference(BaseEnum):
    def _generate_next_value_(name: str, start, count, last_values):
        name = name.replace("_", ".")
        if name.startswith("CO_"):
            name = name.replace("CO", "S")

        return name


class Type(BaseEnum):
    pass


@unique
class UnityType(Type):
    APARTMENT = auto()
    COMERCIAL = auto()


@unique
class Apartment(Reference):
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
class Comercial(Reference):
    CO_01 = auto()
    CO_02 = auto()
    CO_03 = auto()
    CO_04 = auto()


def get_unity_possible_values() -> list:
    return Apartment.values() + Comercial.values()


def check_unity_type(unity_reference: str, unity_type: str) -> bool:
    from src.domain import apartment_string_id, comercial_string_id

    assert isinstance(unity_reference, str), "unity_reference must be a string"

    check_apartment = unity_reference.startswith(apartment_string_id) and unity_type == (
        UnityType.APARTMENT.value
    )
    check_comercial = unity_reference.startswith(comercial_string_id) and unity_type == (
        UnityType.COMERCIAL.value
    )

    return check_apartment or check_comercial
