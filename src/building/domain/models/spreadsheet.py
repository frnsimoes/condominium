from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from src.building.domain.models.unity import Unity


@dataclass(frozen=True)
class Expenses:
    water: Decimal
    energy: Decimal
    fire_energy: Decimal
    internet: Decimal
    cleaner: Decimal
    apartments_utilitaries: Optional[Decimal] = Decimal("0")
    generic_utilitaries: Optional[Decimal] = Decimal("0")


class SpreadsheetType:
    REGULAR = 'regular'
    PROPORTIONAL = 'proportional'


@dataclass
class Spreadsheet:
    expenses: Expenses
    # registered_unities: list = field(default_factory=Unity.registered_unities)

    def calculate_expense_per_unity(self, expense_name: str):
        payers: list = Unity.get_payers_per_expense(expense_name)
        expense: Decimal = getattr(self.expenses, expense_name)
        return expense / len(payers)
