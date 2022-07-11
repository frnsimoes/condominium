# from decimal import Decimal
# from condominium.domain.models.spreadsheet import Spreadsheet
# from condominium.domain.models.unity import BaseUnity


# def calculate_expense_per_unity(spreadsheet: Spreadsheet, expense_name: str):
#     payers: list = BaseUnity.get_payers_per_expense(expense_name)
#     expense: Decimal = getattr(spreadsheet.expenses, expense_name)
#     return expense / len(payers)


# def get_payers_per_expense_name(expense_name: str):
#     return [
#         unity
#         for unity in BaseUnity.registered_unities
#         if getattr(unity.payable_expenses, expense_name)
#     ]
