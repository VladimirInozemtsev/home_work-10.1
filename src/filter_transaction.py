import csv
import json
import logging
import os
from typing import List, Dict
import re
from datetime import datetime

import openpyxl
import read_transactions

# Логгирование
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def filter_transactions_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    """
    Фильтрация транзакций по строке поиска в описании.

    Args:
        transactions: Список словарей с данными о транзакциях.
        search_string: Строка поиска.

    Returns:
        Список словарей с транзакциями, у которых в описании есть строка поиска.
    """
    filtered_transactions = []
    for transaction in transactions:
        if re.search(search_string, transaction['description'], re.IGNORECASE):
            filtered_transactions.append(transaction)
    return filtered_transactions


def count_transactions_by_category(transactions: List[Dict], categories: List[str]) -> Dict:
    """
    Подсчет количества транзакций в каждой категории.

    Args:
        transactions: Список словарей с данными о транзакциях.
        categories: Список категорий операций.

    Returns:
        Словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
    """
    category_counts = {}
    for transaction in transactions:
        for category in categories:
            if category.lower() in transaction['description'].lower():
                if category in category_counts:
                    category_counts[category] += 1
                else:
                    category_counts[category] = 1
    return category_counts


def format_transaction(transaction: Dict) -> str:
    """
    Форматирует данные о транзакции для вывода в консоль.

    Args:
        transaction: Словарь с данными о транзакции.

    Returns:
        Отформатированная строка с данными о транзакции.
    """
    date_obj = datetime.strptime(transaction['date'], '%Y-%m-%dT%H:%M:%SZ')
    formatted_date = date_obj.strftime('%d.%m.%Y')

    from_account = transaction['from']
    to_account = transaction['to']

    amount = f"{transaction['amount']} {transaction['currency_code']}"

    description = transaction['description']

    formatted_transaction = f"{formatted_date} {description}\n"
    if from_account.startswith('Счет'):
        formatted_transaction += f"Счет {from_account[-4:]}\n"
    else:
        formatted_transaction += f"{from_account}\n"
    if to_account.startswith('Счет'):
        formatted_transaction += f"Счет {to_account[-4:]}\n"
    else:
        formatted_transaction += f"{to_account}\n"
    formatted_transaction += f"Сумма: {amount}\n\n"

    return formatted_transaction
