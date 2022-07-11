from decimal import Decimal

import factory

from condominium.domain.models.spreadsheet import Expenses


class ExpensesFactory(factory.Factory):
    class Meta:
        model = Expenses

    water = Decimal("1500")
    energy = Decimal("105.50")
    fire_energy = Decimal("99")
    internet = Decimal("149.90")
    cleaner = Decimal("250")
