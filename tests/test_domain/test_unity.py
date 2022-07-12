import pytest

from condominium.domain import Apartment, ApartmentUnity, Comercial, ComercialUnity, PayableExpenses, Unity
from condominium.domain.exceptions import UnityAlreadyRegistered


@pytest.fixture(autouse=True)
def reset_registered():
    Unity.registered.clear()


def test_unity_is_registered_when_created():
    payable_expenses = PayableExpenses()
    ap_01 = ApartmentUnity(reference=Apartment.AP_01, payable_expenses=payable_expenses)
    assert ap_01 in Unity.registered

    co_01 = ComercialUnity(reference=Comercial.CO_01, payable_expenses=payable_expenses)
    assert co_01 in Unity.registered

    assert len(Unity.registered) == 2


def test_outlaw_registration_of_two_unities_with_came_reference():
    payable_expenses = PayableExpenses()
    first_ap = ApartmentUnity(reference=Apartment.AP_01, payable_expenses=payable_expenses)
    with pytest.raises(UnityAlreadyRegistered):
        ApartmentUnity(reference=Apartment.AP_01, payable_expenses=payable_expenses)

    first_co = ComercialUnity(reference=Comercial.CO_01, payable_expenses=payable_expenses)
    with pytest.raises(UnityAlreadyRegistered) as e:
        ComercialUnity(reference=Comercial.CO_01, payable_expenses=payable_expenses)

    assert len(Unity.registered) == 2
    assert first_co, first_ap in Unity.registered


def test_get_payers_per_expense():
    payable_expenses = PayableExpenses()
    no_water_payable_expenses = PayableExpenses(water=False)
    first_ap = ApartmentUnity(reference=Apartment.AP_01, payable_expenses=payable_expenses)
    first_co = ComercialUnity(reference=Comercial.CO_01, payable_expenses=payable_expenses)
    second_ap = ApartmentUnity(reference=Apartment.AP_02, payable_expenses=payable_expenses)
    second_co = ComercialUnity(reference=Comercial.CO_02, payable_expenses=no_water_payable_expenses)

    payers_per_water = Unity.get_payers_per_expense("water")
    assert first_ap in payers_per_water
    assert second_ap in payers_per_water
    assert first_co in payers_per_water
    assert second_co not in payers_per_water
