from dataclasses import dataclass
from typing import ClassVar

from condominium.domain.exceptions import UnityAlreadyRegistered


@dataclass
class PayableExpenses:
    water: bool = True
    energy: bool = False
    fire_energy: bool = True
    internet: bool = False
    cleaner: bool = True
    apartments_utilitaries: bool = False
    generic_utilitaries: bool = True


@dataclass
class Unity:
    registered: ClassVar[list] = list()
    name: str
    payable_expenses: PayableExpenses

    @classmethod
    def get_payers_per_expense(cls, expense_name: str):
        return [r for r in cls.registered if getattr(r.payable_expenses, expense_name)]

    @classmethod
    def registered_unity_names(cls):
        return [unity.name for unity in cls.registered]

    def __post_init__(self):
        if self.name in Unity.registered_unity_names():
            raise UnityAlreadyRegistered(f"{self.name} is already registered")

        Unity.registered.append(self)
