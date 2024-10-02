import json
import logging
import os


utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Создаем директорию logs
logs_dir = os.path.join(project_dir, "logs")
os.makedirs(logs_dir, exist_ok=True)

utils_file_handler = logging.FileHandler(os.path.join(logs_dir, "utils.log"), mode="w")

utils_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
utils_file_handler.setFormatter(utils_formatter)

utils_logger.addHandler(utils_file_handler)



utils_logger = logging.getLogger(__name__)

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

    utils_logger.debug(f"Попытка чтения транзакций из файла: {filepath}")

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            utils_logger.debug(f"Данные из файла: {data}")
            if isinstance(data, list):
                utils_logger.info(f"Успешное чтение транзакций из файла: {filepath}")
                return data
            else:
                utils_logger.warning(f"Файл {filepath} содержит некорректные данные (не список).")
                return []
    except FileNotFoundError:
        utils_logger.warning(f"Файл {filepath} не найден.")
        return []
    except json.JSONDecodeError:
        utils_logger.error(f"Ошибка декодирования JSON в файле {filepath}.")
        return []


# Получаем путь к файлу operations.json
#filepath = os.path.join(project_dir, "data", "operations.json")

# Вызываем функцию read_transactions_from_json
#transactions = read_transactions_from_json(filepath)
#transactions = [
#    {'id': 1, 'state': 'EXECUTED', 'date': '2023-10-26T10:00:00Z', 'description': 'Перевод на счет'},
#    {'id': 2, 'state': 'CANCELED', 'date': '2023-10-25T14:30:00Z', 'description': 'Покупка в интернет-магазине'},
#    {'id': 3, 'state': 'EXECUTED', 'date': '2023-10-24T12:15:00Z', 'description': 'Оплата услуг'}
#]
#filtered_transactions = [transaction for transaction in transactions if transaction.get("state")]

#print(filtered_transactions)