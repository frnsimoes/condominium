import pytest

from src.building.domain.exceptions import UnityNameAlreadyRegistered
from src.building.domain.models import unity
from src.building.domain.value_object import ApartmentUnities
from tests.factories.unity_factory import AP01Factory, AP02Factory


@pytest.fixture(autouse=True)
def reset_registered():
    unity.Unity.registered_refs.clear()
    unity.Unity.registered_unities.clear()


def test_unit_can_be_created():
    expenses = unity.PayableExpenses()
    name = ApartmentUnities.AP_01.value
    reference = unity.ApartmentUnity(name=name)
    ap = unity.Unity(expenses=expenses, reference=reference)

    assert ap is not None
    assert ap.expenses == expenses
    assert ap.reference == reference


def test_reference_name_can_be_accessed_by_name_property():
    ap = AP01Factory()
    assert ap.name == ap.reference.name


def test_two_unities_with_same_reference_name_cannot_be_created():
    ap_01 = AP01Factory()

    second_expenses = unity.PayableExpenses()
    same_reference = unity.ApartmentUnity(name=ap_01.reference.name)
    with pytest.raises(UnityNameAlreadyRegistered) as e:
        unity.Unity(expenses=second_expenses, reference=same_reference)
    assert str(e.value) == f"{same_reference.name} is already registered"


def test_get_payers_per_expense():
    ap_01 = AP01Factory()

    no_water = unity.PayableExpenses(water=False)
    ap_02 = AP02Factory(expenses=no_water)

    water_payers = unity.Unity.get_payers_per_expense("water")
    assert ap_01 in water_payers
    assert ap_02 not in water_payers
