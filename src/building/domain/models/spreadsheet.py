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
class SpreadSheet:
    expenses: Expenses
    registered_unities: set = Unity.registered
