from src.domain import value_objects


def test_apartment_string_identity(mocker):
    assert value_objects.Apartment.string_identity() == "AP"


def test_comercial_string_identity():
    assert value_objects.Comercial.string_identity() == "CO"
