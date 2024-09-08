import csv
import json
import logging
import os
from typing import List, Dict
import re
from datetime import datetime

import openpyxl
from src.filter_transaction import filter_transactions_by_description, format_transaction
import read_transactions
def main():
    """
    Основная логика программы.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input()

    if choice == '1':
        filepath = input("Для обработки выберите JSON-файл: ")
        try:
            with open(filepath, 'r') as f:
                transactions = json.load(f)
        except FileNotFoundError:
            print(f"Файл {filepath} не найден.")
            return

    elif choice == '2':
        filepath = input("Для обработки выберите CSV-файл: ")
        transactions = read_transactions.read_transactions_from_csv(filepath)

    elif choice == '3':
        filepath = input("Для обработки выберите XLSX-файл: ")
        transactions = read_transactions.read_transactions_from_excel(filepath)

    else:
        print("Неверный выбор пункта меню.")
        return

    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. \n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        ).upper()
        if status in ['EXECUTED', 'CANCELED', 'PENDING']:
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    print(f'Операции отфильтрованы по статусу "{status}"')

    filtered_transactions = [transaction for transaction in transactions if transaction['state'] == status]

    while True:
        sort_by_date = input("Отсортировать операции по дате? Да/Нет\n").lower()
        if sort_by_date in ['да', 'нет']:
            break
        else:
            print("Неверный ввод. Введите 'Да' или 'Нет'.")

    if sort_by_date == 'да':
        while True:
            sort_order = input(
                "Отсортировать по возрастанию или по убыванию? \n"
                "Введите 'по возрастанию' или 'по убыванию':\n"
            ).lower()
            if sort_order in ['по возрастанию', 'по убыванию']:
                break
            else:
                print("Неверный ввод. Введите 'по возрастанию' или 'по убыванию'.")
        if sort_order == 'по возрастанию':
            filtered_transactions = sorted(
                filtered_transactions, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%SZ')
            )
        else:
            filtered_transactions = sorted(
                filtered_transactions, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%SZ'), reverse=True
            )

    while True:
        only_ruble = input("Выводить только рублевые тразакции? Да/Нет\n").lower()
        if only_ruble in ['да', 'нет']:
            break
        else:
            print("Неверный ввод. Введите 'Да' или 'Нет'.")

    if only_ruble == 'да':
        filtered_transactions = [
            transaction for transaction in filtered_transactions if transaction['currency_code'] == 'RUB'
        ]

    while True:
        search_by_description = input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n"
        ).lower()
        if search_by_description in ['да', 'нет']:
            break
        else:
            print("Неверный ввод. Введите 'Да' или 'Нет'.")

    if search_by_description == 'да':
        search_string = input("Введите слово для поиска в описании: ")
        filtered_transactions = filter_transactions_by_description(filtered_transactions, search_string)

    print("Распечатываю итоговый список транзакций...")
    if filtered_transactions:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            print(format_transaction(transaction))
    else:
        print(
            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
        )


if __name__ == "__main__":
    main()