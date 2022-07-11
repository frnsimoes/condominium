from dataclasses import dataclass
from typing import List, Literal

from condominium.domain.exceptions import UnityAlreadyRegistered


@dataclass(frozen=True)
class PayableExpenses:
    water: bool = True
    energy: bool = False
    fire_energy: bool = True
    internet: bool = False
    cleaner: bool = True
    apartments_utilitaries: bool = False
    generic_utilitaries: bool = True


class Unity:
    registered: list = list()

    def __init__(self, reference, payable_expenses):
        self.reference = reference
        self.payable_expenses = payable_expenses

        if self.reference.name in Unity.get_unity_names():
            raise UnityAlreadyRegistered(f"{self.reference} is already registered")

    @classmethod
    def get_payers_per_expense(cls, expense_name: str):
        return [r for r in cls.registered if getattr(r.payable_expenses, expense_name)]

    @classmethod
    def get_unity_names(cls):
        return [unity.reference.name for unity in cls.registered]


@dataclass(unsafe_hash=True)
class ApartmentUnity(Unity):
    reference: Literal
    payable_expenses: PayableExpenses

    def __post_init__(self):
        super().__init__(self.reference, self.payable_expenses)
        super().registered.append(self)

    @property
    def has_gas(self):
        return True


@dataclass(unsafe_hash=True)
class ComercialUnity(Unity):
    reference: Literal
    payable_expenses: PayableExpenses

    def __post_init__(self):
        super().__init__(self.reference, self.payable_expenses)

        if self.payable_expenses.energy:
            raise Exception()

        if self.payable_expenses.apartments_utilitaries:
            raise Exception()

        super().registered.append(self)

    @property
    def has_gas(self):
        return False
