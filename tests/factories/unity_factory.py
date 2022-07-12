import factory

from condominium.domain.models.unity import ApartmentUnity, BaseUnity, ComercialUnity, PayableExpenses
from condominium.domain.value_object import Apartment, Comercial


class AP01Factory(factory.Factory):
    class Meta:
        model = BaseUnity

    expenses = PayableExpenses()
    reference = ApartmentUnity(name=Apartment.AP_01.value)


class AP02Factory(factory.Factory):
    class Meta:
        model = BaseUnity

    expenses = PayableExpenses()
    reference = ApartmentUnity(name=Apartment.AP_02.value)


class AP03Factory(factory.Factory):
    class Meta:
        model = BaseUnity

    expenses = PayableExpenses()
    reference = ApartmentUnity(name=Apartment.AP_03.value)


class S01Factory(factory.Factory):
    class Meta:
        model = BaseUnity

    expenses = PayableExpenses()
    reference = ComercialUnity(name=Comercial.CO_01.value)


class S02Factory(factory.Factory):
    class Meta:
        model = BaseUnity

    expenses = PayableExpenses()
    reference = ComercialUnity(name=Comercial.CO_02.value)
