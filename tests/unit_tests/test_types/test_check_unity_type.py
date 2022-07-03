from src.domain import _types


def test_apartment_success():
    unity_reference = _types.Apartment.AP_01.value
    unity_type = _types.UnityType.APARTMENT.value

    check = _types.check_unity_type(unity_reference, unity_type)
    assert check is True


def test_apartment_unity_reference_insuccess():
    unity_reference = _types.Comercial.CO_01.value
    unity_type = _types.UnityType.APARTMENT.value

    check = _types.check_unity_type(unity_reference, unity_type)
    assert check is False


def test_apartment_unity_type_insuccess():
    unity_reference = _types.Apartment.AP_01.value
    unity_type = _types.UnityType.COMERCIAL.value

    check = _types.check_unity_type(unity_reference, unity_type)
    assert check is False


def test_comercial_success():
    unity_reference = _types.Comercial.CO_01.value
    unity_type = _types.UnityType.COMERCIAL.value

    check = _types.check_unity_type(unity_reference, unity_type)
    assert check is True


def test_comercial_unity_reference_insuccess():
    unity_reference = _types.Apartment.AP_01.value
    unity_type = _types.UnityType.COMERCIAL.value

    check = _types.check_unity_type(unity_reference, unity_type)
    assert check is False


def test_comercial_unity_type_insuccess():
    unity_reference = _types.Comercial.CO_01.value
    unity_type = _types.UnityType.APARTMENT.value

    check = _types.check_unity_type(unity_reference, unity_type)
    assert check is False
