from src.domain import _types


def test_unity_possible_values():
    possible_values = [e.value for e in _types.Apartment] + [
        e.value for e in _types.Comercial
    ]
    assert possible_values == _types.get_unity_possible_values()
