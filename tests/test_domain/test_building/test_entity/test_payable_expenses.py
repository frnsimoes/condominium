from dataclasses import FrozenInstanceError

import pytest

from src.domain.building.entity import PayableExpenses


def test_payable_expenses_cannot_be_modified_after_creation():
    expenses = PayableExpenses()
    assert expenses is not None

    with pytest.raises(FrozenInstanceError):
        expenses.energy = False
