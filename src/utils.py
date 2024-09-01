import json
import os

def read_transactions_from_json(filepath):
    """
    Читает данные о финансовых транзакциях из JSON-файла.

    Args:
        filepath: Путь к JSON-файлу с данными о транзакциях.

    Returns:
        Список словарей с данными о транзакциях.
        Если файл пустой, содержит не список или не найден,
        функция возвращает пустой список.
    """

    try:
        with open(filepath, "r") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    except:
        return []
