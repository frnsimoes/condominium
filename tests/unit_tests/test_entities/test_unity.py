from src.constants import Type
from src.entities import PayableExpenses, Unity
import pytest


@pytest.fixture(autouse=True)
def reset_registered():
    Unity._registered.clear()


def test_unity_is_created():
    expenses = PayableExpenses()
    type = Type.APARTMENT.value
    unity = Unity(type=type, expenses=expenses, reference="AP. 01")

    assert unity is not None
    assert unity.type == "APARTMENT"
    assert unity.reference == "AP. 01"


def test_two_unities_with_same_reference_cannot_be_created():
    expenses = PayableExpenses()
    type = Type.APARTMENT.value
    first_unity = Unity(type=type, expenses=expenses, reference="AP. 01")
    assert first_unity is not None

    second_expenses = PayableExpenses()
    second_type = Type.APARTMENT.value
    with pytest.raises(Exception) as e:
        second_unity = Unity(  # noqa F841
            type=second_type, expenses=second_expenses, reference="AP. 01"
        )
    assert str(e.value) == "reference already registered"


def test_invalid_reference_raises_error():
    expenses = PayableExpenses()
    type = Type.APARTMENT.value

    with pytest.raises(Exception) as e:
        Unity(type=type, expenses=expenses, reference="invalid reference")
    assert str(e.value) == "reference is not a possible value"
