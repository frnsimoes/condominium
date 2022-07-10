import factory

from src.building.domain.models.unity import ApartmentUnity, ComercialUnity, PayableExpenses, Unity
from src.building.domain.value_object import ApartmentUnities, ComercialUnities


class AP01Factory(factory.Factory):
    class Meta:
        model = Unity

    expenses = PayableExpenses()
    reference = ApartmentUnity(name=ApartmentUnities.AP_01.value)


class AP02Factory(factory.Factory):
    class Meta:
        model = Unity

    expenses = PayableExpenses()
    reference = ApartmentUnity(name=ApartmentUnities.AP_02.value)


class AP03Factory(factory.Factory):
    class Meta:
        model = Unity

    expenses = PayableExpenses()
    reference = ApartmentUnity(name=ApartmentUnities.AP_03.value)


class S01Factory(factory.Factory):
    class Meta:
        model = Unity

    expenses = PayableExpenses()
    reference = ComercialUnity(name=ComercialUnities.CO_01.value)


class S02Factory(factory.Factory):
    class Meta:
        model = Unity

    expenses = PayableExpenses()
    reference = ComercialUnity(name=ComercialUnities.CO_02.value)
