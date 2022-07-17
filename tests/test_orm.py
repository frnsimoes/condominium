from condominium.domain import Unity
from condominium.domain.models.unity import PayableExpenses
from condominium.domain.value_object import Apartment


def test_unity_mapper_can_load(session):
    ap_01 = Unity(name=Apartment.AP_01.value, payable_expenses=PayableExpenses())
    ap_02 = Unity(name=Apartment.AP_02.value, payable_expenses=PayableExpenses())
    session.add_all([ap_01, ap_02])
    session.commit()

    expected = [ap_01, ap_02]
    assert session.query(Unity).all() == expected
