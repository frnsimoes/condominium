from dataclasses import dataclass
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
    apartments_utilitaries: Optional[Decimal]
    generic_utilitaries: Optional[Decimal]


@dataclass
class Spreadsheet:
    expenses: Expenses
    registered_unities: list = Unity.registered_unities

    @property
    def water_sum_per_payer(self):
        return self.expenses.water / len(Unity.water_payers())
