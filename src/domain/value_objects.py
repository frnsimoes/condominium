from src.domain import _types


class Apartment:
    _MAX_CAPACITY = 12
    _HAS_GAS = False

    @staticmethod
    def string_identity():
        return _types.Apartment.__name__.upper()[:2]


class Comercial:
    _MAX_CAPACITY = 4
    _HAS_GAS = True

    @staticmethod
    def string_identity():
        return _types.Comercial.__name__.upper()[:2]
