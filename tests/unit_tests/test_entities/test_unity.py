from src.domain._types import Apartment, UnityType
from src.domain.entities import PayableExpenses, Unity
import pytest


@pytest.fixture(autouse=True)
def reset_registered():
    Unity._registered.clear()


def test_unity_is_created():
    expenses = PayableExpenses()
    type = UnityType.APARTMENT.value
    reference = Apartment.AP_01.value
    unity = Unity(type=type, expenses=expenses, reference=reference)

    assert unity is not None
    assert unity.type == "APARTMENT"
    assert unity.reference == reference


def test_two_unities_with_same_reference_cannot_be_created():
    expenses = PayableExpenses()
    type = UnityType.APARTMENT.value
    reference = Apartment.AP_01.value
    first_unity = Unity(type=type, expenses=expenses, reference=reference)
    assert first_unity is not None

    second_expenses = PayableExpenses()
    second_type = UnityType.APARTMENT.value
    second_reference = Apartment.AP_01.value
    with pytest.raises(Exception) as e:
        second_unity = Unity(  # noqa F841
            type=second_type, expenses=second_expenses, reference=second_reference
        )
    assert str(e.value) == "reference already registered"


def test_invalid_reference_raises_error():
    expenses = PayableExpenses()
    type = UnityType.APARTMENT.value

    with pytest.raises(Exception) as e:
        Unity(type=type, expenses=expenses, reference="invalid reference")
    assert str(e.value) == "reference is not a possible value"


def test_invalid_type_raises_error():
    expenses = PayableExpenses()
    reference = Apartment.AP_01.value

    with pytest.raises(Exception) as e:
        Unity(type="invalid type", expenses=expenses, reference=reference)
    assert str(e.value) == "Type must be Apartment or Comercial"
