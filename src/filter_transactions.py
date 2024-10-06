import re
from typing import List, Dict


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
        if re.search(search_string, transaction["description"], re.IGNORECASE):
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
            if category.lower() in transaction["description"].lower():
                if category in category_counts:
                    category_counts[category] += 1
                else:
                    category_counts[category] = 1
    return category_counts
