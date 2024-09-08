import csv
from typing import List, Dict
import openpyxl


def read_transactions_from_csv(filepath: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV-файла.

    Args:
        filepath: Путь к CSV-файлу.

    Returns:
        Список словарей с данными о транзакциях.
    """
    transactions = []
    with open(filepath, "r", encoding="utf-8", newline="") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            transactions.append(row)
    return transactions


def read_transactions_from_excel(filepath: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel-файла.

    Args:
        filepath: Путь к Excel-файлу.

    Returns:
        Список словарей с данными о транзакциях.
    """
    transactions = []
    workbook = openpyxl.load_workbook(filepath)
    worksheet = workbook.active
    # Пропускаем первую строку с заголовками
    for row in worksheet.iter_rows(min_row=2, values_only=True):
        transactions.append(
            {
                "id": row[0],
                "state": row[1],
                "date": row[2],
                "amount": row[3],
                "currency_name": row[4],
                "currency_code": row[5],
                "from": row[6],
                "to": row[7],
                "description": row[8],
            }
        )
    return transactions
