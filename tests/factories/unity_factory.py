import factory

from src.building.domain.models.unity import ApartmentUnity, PayableExpenses, Unity
from src.building.domain.value_object import ApartmentUnities


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
