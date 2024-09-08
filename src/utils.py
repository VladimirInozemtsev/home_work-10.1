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
                return data  # return внутри функции
            else:
                utils_logger.warning(f"Файл {filepath} содержит некорректные данные (не список).")
                return []  # return внутри функции
    except FileNotFoundError:
        utils_logger.warning(f"Файл {filepath} не найден.")
        return []  # return внутри функции
    except json.JSONDecodeError:
        utils_logger.error(f"Ошибка декодирования JSON в файле {filepath}.")
        return []  # return внутри функции


# Получаем путь к файлу operations.json
filepath = os.path.join(project_dir, "data", "operations.json")

# Вызываем функцию read_transactions_from_json
transactions = read_transactions_from_json(filepath)
