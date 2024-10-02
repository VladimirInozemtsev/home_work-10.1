import logging
from datetime import datetime
import os
from utils import read_transactions_from_json
from read_transactions import read_transactions_from_excel, read_transactions_from_csv
import re
from collections import Counter


utils_logger = logging.getLogger(__name__)


def filter_transactions_by_status(transactions, status):
    """
    Фильтрация транзакций по статусу.

    Args:
        transactions: Список словарей с транзакциями.
        status: Статус для фильтрации.

    Returns:
        Список словарей с отфильтрованными транзакциями.
    """
    status = status.upper()
    utils_logger.debug(f"Фильтрация транзакций по статусу: {status}")
    return [transaction for transaction in transactions if transaction.get("state") == status]


def filter_transactions_by_word(transactions, word):
    """
    Фильтрация транзакций по наличию слова в описании.

    Использует регулярное выражение для поиска слова в описании,
    независимо от регистра.

    Args:
        transactions: Список словарей с транзакциями.
        word: Слово для поиска в описании.

    Returns:
        Список словарей с отфильтрованными транзакциями.
    """
    utils_logger.debug(f"Фильтрация транзакций по слову в описании: {word}")
    pattern = re.compile(word, re.IGNORECASE)

    return [transaction for transaction in transactions if pattern.search(transaction['description'])]


def sort_transactions_by_date(transactions, order):
    """
    Сортировка транзакций по дате.

    Args:
        transactions: Список словарей с транзакциями.
        order: Порядок сортировки (asc - по возрастанию, desc - по убыванию).

    Returns:
        Список отсортированных словарей с транзакциями.
    """
    utils_logger.debug(f"Сортировка транзакций по дате: {order}")
    if order == "по возрастанию":
        return sorted(transactions, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%SZ'))
    elif order == "по убыванию":
        return sorted(transactions, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%SZ'), reverse=True)
    else:
        utils_logger.warning(f"Неверный порядок сортировки: {order}. Возвращаю исходный список")
        return transactions


def filter_transactions_by_currency(transactions):
    """
    Фильтрация транзакций по валюте.

    Args:
        transactions: Список словарей с транзакциями.

    Returns:
        Список словарей с отфильтрованными транзакциями.
    """
    utils_logger.debug(f"Фильтрация транзакций по валюте: RUB")
    return [transaction for transaction in transactions if
            "operationAmount" in transaction and transaction["operationAmount"]["currency"]["code"] == "RUB"]


def count_transactions_by_category(transactions, categories):
    """
    Подсчет количества операций по каждой категории.

    Args:
        transactions: Список словарей с транзакциями.
        categories: Список категорий операций.

    Returns:
        Словарь, где ключ — название категории, значение — количество операций.
    """
    utils_logger.debug(f"Подсчет количества операций по категориям: {categories}")
    category_counts = Counter()  # Используем Counter для подсчета
    for transaction in transactions:
        for category in categories:
            if category.lower() in transaction["description"].lower():
                category_counts[category] += 1
    return dict(category_counts)


def format_transaction(transaction):
    """
    Форматирует данные о транзакции для вывода в консоль.

    Args:
        transaction: Словарь с данными о транзакции.

    Returns:
        Отформатированная строка с данными о транзакции.
    """
    date_obj = datetime.strptime(transaction['date'], '%Y-%m-%dT%H:%M:%SZ')
    formatted_date = date_obj.strftime('%d.%m.%Y')

    from_account = transaction.get('from')  # Используйте .get()
    to_account = transaction.get('to')

    # Извлечение значения amount из разных форматов
    if "operationAmount" in transaction:
        amount = f"{transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['code']}"
    elif "amount" in transaction:
        amount = f"{transaction['amount']} {transaction['currency_code']}"  # Предположим, что в CSV и XLSX "amount" и "currency_code" отдельные ключи
    else:
        amount = "Неизвестная сумма"

    description = transaction['description']

    formatted_transaction = f"{formatted_date} {description}\n"

    if from_account is not None:
        if from_account.startswith('Счет'):
            formatted_transaction += f"Счет {from_account[-4:]}\n"
        else:
            formatted_transaction += f"{from_account}\n"

    if to_account is not None:
        if to_account.startswith('Счет'):
            formatted_transaction += f"Счет {to_account[-4:]}\n"
        else:
            formatted_transaction += f"{to_account}\n"

    formatted_transaction += f"Сумма: {amount}\n\n"

    return formatted_transaction


def main():
    """
    Основная функция программы.
    """
    logging.basicConfig(level=logging.DEBUG)
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, '..', 'data')

    while True:
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        choice = input()
        if choice == '1':
            filepath = os.path.join(data_dir, 'operations.json')
            transactions = read_transactions_from_json(filepath)
            break
        elif choice == '2':
            filepath = os.path.join(data_dir, 'transactions.csv')
            transactions = read_transactions_from_csv(filepath)
            break
        elif choice == '3':
            filepath = os.path.join(data_dir, 'transactions_excel.xlsx')
            transactions = read_transactions_from_excel(filepath)
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите пункт меню из списка.")

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = input()
        transactions = filter_transactions_by_status(transactions, status)
        if transactions:
            break
        else:
            print(f"Статус операции \"{status}\" недоступен.")

    print(f"Операции отфильтрованы по статусу \"{status}\"")

    sort_by_date = input("Отсортировать операции по дате? Да/Нет: ").lower() == 'да'
    if sort_by_date:
        while True:
            order = input("Отсортировать по возрастанию или по убыванию? (по возрастанию/по убыванию): ").lower()
            transactions = sort_transactions_by_date(transactions, order)
            if transactions:
                break
            else:
                print(f"Неверный порядок сортировки: {order}")

    filter_by_currency = input("Выводить только рублевые транзакции? Да/Нет: ").lower() == 'да'
    if filter_by_currency:
        transactions = filter_transactions_by_currency(transactions)

    filter_by_word = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower() == 'да'
    if filter_by_word:
        word = input("Введите слово для поиска: ")
        transactions = filter_transactions_by_word(transactions, word)

    print("Распечатываю итоговый список транзакций...")
    if transactions:
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        for i, transaction in enumerate(transactions):
            print(f"{i + 1}. {format_transaction(transaction)}")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    categories = ["Перевод", "Открытие вклада", "Перевод организации"]
    category_counts = count_transactions_by_category(transactions, categories)
    print("\nКоличество операций по категориям:")
    for category, count in category_counts.items():
        print(f"{category}: {count}")


if __name__ == "__main__":
    main()