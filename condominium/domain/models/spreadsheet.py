from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from condominium.domain import Unity


@dataclass(frozen=True)
class Expenses:
    water: Decimal
    energy: Decimal
    fire_energy: Decimal
    internet: Decimal
    cleaner: Decimal
    apartments_utilitaries: Optional[Decimal] = Decimal("0")
    generic_utilitaries: Optional[Decimal] = Decimal("0")


# class SpreadsheetType:
#     REGULAR = "regular"
#     PROPORTIONAL = "proportional"


@dataclass(frozen=True)
class Spreadsheet:
    expenses: Expenses
    _registered_unities: List[Unity] = field(default=Unity.registered)

    def get_expense_value_for_registered_unity(self, expense_name: str):
        expense_payers = Unity.get_payers_per_expense(expense_name)
        return getattr(self.expenses, expense_name) / len(expense_payers)
