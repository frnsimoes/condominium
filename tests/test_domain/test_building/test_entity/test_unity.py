import pytest

from src.building.domain.models import unity
from src.building.domain.exceptions import UnityNameAlreadyRegistered
from src.building.domain.value_object import ApartmentUnities


@pytest.fixture(autouse=True)
def reset_registered():
    unity.Unity.registered.clear()


def test_unit_can_be_created():
    expenses = unity.PayableExpenses()
    name = ApartmentUnities.AP_01.value
    reference = unity.ApartmentUnity(name=name)
    ap = unity.Unity(expenses=expenses, reference=reference)

    assert ap is not None
    assert ap.expenses == expenses
    assert ap.reference == reference


def test_reference_name_can_be_accessed_by_name_property():
    expenses = unity.PayableExpenses()
    name = ApartmentUnities.AP_01.value
    reference = unity.ApartmentUnity(name=name)
    ap = unity.Unity(expenses=expenses, reference=reference)

    assert ap.name == ap.reference.name


def test_two_unities_with_same_reference_name_cannot_be_created():
    expenses = unity.PayableExpenses()
    name = ApartmentUnities.AP_01.value
    reference = unity.ApartmentUnity(name=name)
    ap = unity.Unity(expenses=expenses, reference=reference)
    assert ap is not None

    second_expenses = unity.PayableExpenses()
    same_name = ApartmentUnities.AP_01.value
    same_reference = unity.ApartmentUnity(name=same_name)

    with pytest.raises(UnityNameAlreadyRegistered) as e:
        unity.Unity(expenses=second_expenses, reference=same_reference)
    assert str(e.value) == f"{same_reference.name} is already registered"
