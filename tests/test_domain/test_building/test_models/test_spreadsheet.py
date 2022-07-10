from decimal import Decimal

import pytest

from src.building.domain.models.spreadsheet import Spreadsheet
from src.building.domain.models.unity import PayableExpenses, Unity
from tests.factories.expenses_factory import ExpensesFactory
from tests.factories.unity_factory import AP01Factory, AP02Factory, S01Factory


@pytest.fixture(autouse=True)
def setup():
    no_water_expenses = PayableExpenses(water=False)
    water_expenses = PayableExpenses()
    AP01Factory(expenses=no_water_expenses)
    AP02Factory(expenses=water_expenses)
    S01Factory(expenses=water_expenses)
    Unity.registered_refs.clear()


def test_calculate_bill_per_expense():
    assert len(Unity.registered_unities) == 3
    assert len(Unity.get_payers_per_expense("water")) == 2
    expenses = ExpensesFactory()
    spreadsheet = Spreadsheet(expenses=expenses)

    expected = spreadsheet.expenses.water / 2
    got = spreadsheet.calculate_expense_per_unity("water")
    assert expected == got


def test_calculate_generics():
    expenses = ExpensesFactory()
    spreadsheet = Spreadsheet(expenses=expenses)

    got = spreadsheet.calculate_expense_per_unity("generic_utilitaries")
    assert got == Decimal("0")
