import pytest

from src.building.domain import entity
from src.building.domain.exceptions import UnityNameAlreadyRegistered
from src.building.domain.value_object import ApartmentUnities


@pytest.fixture(autouse=True)
def reset_registered():
    entity.Unity._registered.clear()


def test_unit_can_be_created():
    expenses = entity.PayableExpenses()
    name = ApartmentUnities.AP_01.value
    reference = entity.ApartmentUnity(name=name)
    ap = entity.Unity(expenses=expenses, reference=reference)

    assert ap is not None
    assert ap.expenses == expenses
    assert ap.reference == reference


def test_reference_name_can_be_accessed_by_name_property():
    expenses = entity.PayableExpenses()
    name = ApartmentUnities.AP_01.value
    reference = entity.ApartmentUnity(name=name)
    ap = entity.Unity(expenses=expenses, reference=reference)

    assert ap.name == ap.reference.name


def test_two_unities_with_same_reference_name_cannot_be_created():
    expenses = entity.PayableExpenses()
    name = ApartmentUnities.AP_01.value
    reference = entity.ApartmentUnity(name=name)
    ap = entity.Unity(expenses=expenses, reference=reference)
    assert ap is not None

    second_expenses = entity.PayableExpenses()
    same_name = ApartmentUnities.AP_01.value
    same_reference = entity.ApartmentUnity(name=same_name)

    with pytest.raises(UnityNameAlreadyRegistered) as e:
        entity.Unity(expenses=second_expenses, reference=same_reference)
    assert str(e.value) == f"{same_reference.name} is already registered"
