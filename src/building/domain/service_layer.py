from building.domain.models.unity import Unity
from src.building.domain.models.spreadsheet import SpreadSheet


def test_calculate_default_expenses():
    # Pegar quantidade de unidades por pagante de despesa.
    # Dividir o total da despesa pelo total de pagantes.
    ...


def calculate_water(spreadsheet: SpreadSheet):
    water_payers: list = Unity.water_payers()
    total = spreadsheet.expenses.water / len(water_payers)
    return total

    ...
