import unittest
from unittest.mock import patch
import io
import json
import datetime
from src.filter_transactions import filter_transactions_by_description, format_transaction, count_transactions_by_category
from src.main import main

class TestMain(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', 'test.json', 'EXECUTED', 'да', 'по возрастанию', 'да', 'да', 'да', 'перевод'])
    @patch('json.load', return_value=[
        {'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210', 'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
        {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': '29740', 'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
        {'id': '593027', 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': '30368', 'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'},
        {'id': '366176', 'state': 'EXECUTED', 'date': '2020-08-02T09:35:18Z', 'amount': '29482', 'currency_name': 'Rupiah', 'currency_code': 'IDR', 'from': 'Discover 0325955596714937', 'to': 'Visa 3820488829287420', 'description': 'Перевод с карты на карту'},
    ])
    @patch('builtins.print')
    def test_main_json(self, mock_print, mock_json_load, mock_input):
        main.main()  # Вызовите функцию main
        mock_print.assert_any_call("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
        mock_print.assert_any_call("Выберите необходимый пункт меню:")
        mock_print.assert_any_call("1. Получить информацию о транзакциях из JSON-файла")
        mock_print.assert_any_call("2. Получить информацию о транзакциях из CSV-файла")
        mock_print.assert_any_call("3. Получить информацию о транзакциях из XLSX-файла")
        mock_print.assert_any_call("Для обработки выберите JSON-файл: ")
        mock_print.assert_any_call('Операции отфильтрованы по статусу "EXECUTED"')
        mock_print.assert_any_call("Отсортировать операции по дате? Да/Нет")
        mock_print.assert_any_call("Отсортировать по возрастанию или по убыванию? ")
        mock_print.assert_any_call("Выводить только рублевые тразакции? Да/Нет")
        mock_print.assert_any_call("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        mock_print.assert_any_call("Распечатываю итоговый список транзакций...")
        mock_print.assert_any_call("Всего банковских операций в выборке: 1")

    @patch('builtins.input', side_effect=['2', 'test.csv', 'EXECUTED', 'да', 'по убыванию', 'нет', 'нет', 'test'])
    @patch('read_transactions.read_transactions_from_csv', return_value=[
        {'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210', 'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
        {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': '29740', 'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
        {'id': '593027', 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': '30368', 'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'},
        {'id': '366176', 'state': 'EXECUTED', 'date': '2020-08-02T09:35:18Z', 'amount': '29482', 'currency_name': 'Rupiah', 'currency_code': 'IDR', 'from': 'Discover 0325955596714937', 'to': 'Visa 3820488829287420', 'description': 'Перевод с карты на карту'},
    ])
    @patch('builtins.print')
    def test_main_csv(self, mock_print, mock_read_transactions_from_csv, mock_input):
        main.main()  # Вызовите функцию main
        mock_print.assert_any_call("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
        mock_print.assert_any_call("Выберите необходимый пункт меню:")
        mock_print.assert_any_call("1. Получить информацию о транзакциях из JSON-файла")
        mock_print.assert_any_call("2. Получить информацию о транзакциях из CSV-файла")
        mock_print.assert_any_call("3. Получить информацию о транзакциях из XLSX-файла")
        mock_print.assert_any_call("Для обработки выберите CSV-файл: ")
        mock_print.assert_any_call('Операции отфильтрованы по статусу "EXECUTED"')
        mock_print.assert_any_call("Отсортировать операции по дате? Да/Нет")
        mock_print.assert_any_call("Отсортировать по возрастанию или по убыванию? ")
        mock_print.assert_any_call("Выводить только рублевые тразакции? Да/Нет")
        mock_print.assert_any_call("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        mock_print.assert_any_call("Распечатываю итоговый список транзакций...")
        mock_print.assert_any_call("Всего банковских операций в выборке: 2")

    @patch('builtins.input', side_effect=['3', 'test.xlsx', 'EXECUTED', 'нет', 'нет', 'нет', 'нет'])
    @patch('read_transactions.read_transactions_from_excel', return_value=[
        {'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210', 'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
        {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': '29740', 'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
        {'id': '593027', 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': '30368', 'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'},
        {'id': '366176', 'state': 'EXECUTED', 'date': '2020-08-02T09:35:18Z', 'amount': '29482', 'currency_name': 'Rupiah', 'currency_code': 'IDR', 'from': 'Discover 0325955596714937', 'to': 'Visa 3820488829287420', 'description': 'Перевод с карты на карту'},
    ])
    @patch('builtins.print')
    def test_main_xlsx(self, mock_print, mock_read_transactions_from_excel, mock_input):
        main.main()  # Вызовите функцию main
        mock_print.assert_any_call("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
        mock_print.assert_any_call("Выберите необходимый пункт меню:")
        mock_print.assert_any_call("1. Получить информацию о транзакциях из JSON-файла")
        mock_print.assert_any_call("2. Получить информацию о транзакциях из CSV-файла")
        mock_print.assert_any_call("3. Получить информацию о транзакциях из XLSX-файла")
        mock_print.assert_any_call("Для обработки выберите XLSX-файл: ")
        mock_print.assert_any_call('Операции отфильтрованы по статусу "EXECUTED"')
        mock_print.assert_any_call("Распечатываю итоговый список транзакций...")
        mock_print.assert_any_call("Всего банковских операций в выборке: 2")

    def test_filter_transactions_by_description(self):
        transactions = [
            {'description': 'Перевод с карты на карту'},
            {'description': 'Открытие вклада'},
            {'description': 'Перевод организации'},
        ]
        search_string = 'перевод'
        filtered_transactions = main.filter_transactions_by_description(transactions, search_string)  # Вызовите функцию
        self.assertEqual(len(filtered_transactions), 2)
        self.assertTrue(all('перевод' in transaction['description'].lower() for transaction in filtered_transactions))

    def test_count_transactions_by_category(self):
        transactions = [
            {'description': 'Перевод с карты на карту'},
            {'description': 'Открытие вклада'},
            {'description': 'Перевод организации'},
            {'description': 'Перевод с карты на карту'},
        ]
        categories = ['Перевод', 'Открытие']
        category_counts = main.count_transactions_by_category(transactions, categories)  # Вызовите функцию
        self.assertEqual(category_counts['Перевод'], 3)
        self.assertEqual(category_counts['Открытие'], 1)

    def test_format_transaction(self):
        transaction = {
            'date': '2023-09-05T11:30:32Z',
            'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397',
            'amount': '16210',
            'currency_code': 'PEN',
            'description': 'Перевод организации'
        }
        formatted_transaction = main.format_transaction(transaction)  # Вызовите функцию
        self.assertIn("05.09.2023", formatted_transaction)
        self.assertIn("Перевод организации", formatted_transaction)
        self.assertIn("Счет **3391", formatted_transaction)
        self.assertIn("Счет **9397", formatted_transaction)
        self.assertIn("Сумма: 16210 PEN", formatted_transaction)

if __name__ == '__main__':
    unittest.main()