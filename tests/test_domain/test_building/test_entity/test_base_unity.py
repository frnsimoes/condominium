import pytest

from src.building.domain.models.unity import (
    ApartmentUnities,
    ApartmentUnity,
    BaseUnity,
    ComercialUnities,
    ComercialUnity,
)
from src.building.domain.exceptions import InvalidUnityName


def test_apartment_unity_can_be_created():
    name = ApartmentUnities.AP_01.value
    unity = ApartmentUnity(name=name)

    assert unity is not None


def test_comercial_unity_can_be_created():
    name = ComercialUnities.CO_01.value
    unity = ComercialUnity(name=name)

    assert unity is not None


def test_invalid_name_raises_invalid_unity_name_exception():
    name = "invalid name"
    with pytest.raises(InvalidUnityName) as e:
        ApartmentUnity(name=name)

    assert str(e.value) == "invalid name is not a possible value for ApartmentUnities"


def test_available_unities():
    assert ComercialUnity.available_unities() == 4
    assert ApartmentUnity.available_unities() == 12


def test_string_id():
    assert ComercialUnity.string_id() == "CO"
    assert ApartmentUnity.string_id() == "AP"


def test_subclass_with_no_type_raises_assertion_error():
    class FakeSubclass(BaseUnity):
        pass

    name = ApartmentUnities.AP_01.value
    with pytest.raises(AssertionError) as e:
        FakeSubclass(name=name)

    assert str(e.value) == "class variable _TYPE must be implemented"
