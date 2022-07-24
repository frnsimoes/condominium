from sqlalchemy.orm import Session

from condominium.adapters import repository
from condominium.domain import Unity
from condominium.domain.models.unity import PayableExpenses
from condominium.domain.value_object import Apartment


def test_unity_mapper_can_load(session: Session):
    payable_expenses = PayableExpenses()
    ap_01 = Unity(name=Apartment.AP_01.name, payable_expenses=payable_expenses)
    ap_02 = Unity(name=Apartment.AP_02.name, payable_expenses=payable_expenses)
    session.add_all([ap_01, ap_02])
    session.commit()

    expected = [ap_01, ap_02]
    query = session.query(Unity)
    assert query.all() == expected

    assert query.first().water == payable_expenses.water
    assert query.first().name == "AP_01"

    query = session.query(Unity).filter_by(name=ap_01.name).first()
    assert query == ap_01


def test_repository(session: Session):
    payable_expenses = PayableExpenses()
    ap_03 = Unity(name=Apartment.AP_03.name, payable_expenses=payable_expenses)

    repo = repository.SqlRepository(session)
    repo.add(ap_03)

    query = repo.get(ap_03.name)
    assert query == ap_03
