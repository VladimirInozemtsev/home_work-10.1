import unittest
from src.main import (
    filter_transactions_by_status,
    filter_transactions_by_word,
    sort_transactions_by_date,
    filter_transactions_by_currency,
    count_transactions_by_category,
    format_transaction,
)
from datetime import datetime


class TestBankingTransactions(unittest.TestCase):

    def test_filter_transactions_by_status(self):
        transactions = [
            {"state": "EXECUTED"},
            {"state": "CANCELED"},
            {"state": "PENDING"},
            {"state": "EXECUTED"},
            {"state": "CANCELED"},
        ]
        expected_transactions = [{"state": "EXECUTED"}, {"state": "EXECUTED"}]
        self.assertEqual(filter_transactions_by_status(transactions, "EXECUTED"), expected_transactions)

    def test_filter_transactions_by_word(self):
        transactions = [
            {"description": "Перевод на карту"},
            {"description": "Открытие вклада"},
            {"description": "Перевод организации"},
        ]
        expected_transactions = [{"description": "Перевод на карту"}, {"description": "Перевод организации"}]
        self.assertEqual(filter_transactions_by_word(transactions, "Перевод"), expected_transactions)

    def test_sort_transactions_by_date_asc(self):
        transactions = [
            {"date": "2023-04-01T12:00:00Z"},
            {"date": "2023-03-15T10:00:00Z"},
            {"date": "2023-04-10T14:00:00Z"},
        ]
        expected_transactions = [
            {"date": "2023-03-15T10:00:00Z"},
            {"date": "2023-04-01T12:00:00Z"},
            {"date": "2023-04-10T14:00:00Z"},
        ]
        self.assertEqual(sort_transactions_by_date(transactions, "по возрастанию"), expected_transactions)

    def test_sort_transactions_by_date_desc(self):
        transactions = [
            {"date": "2023-04-01T12:00:00Z"},
            {"date": "2023-03-15T10:00:00Z"},
            {"date": "2023-04-10T14:00:00Z"},
        ]
        expected_transactions = [
            {"date": "2023-04-10T14:00:00Z"},
            {"date": "2023-04-01T12:00:00Z"},
            {"date": "2023-03-15T10:00:00Z"},
        ]
        self.assertEqual(sort_transactions_by_date(transactions, "по убыванию"), expected_transactions)

    def test_filter_transactions_by_currency(self):
        transactions = [
            {"operationAmount": {"currency": {"code": "RUB"}}},
            {"operationAmount": {"currency": {"code": "USD"}}},
            {"operationAmount": {"currency": {"code": "RUB"}}},
        ]
        expected_transactions = [
            {"operationAmount": {"currency": {"code": "RUB"}}},
            {"operationAmount": {"currency": {"code": "RUB"}}},
        ]
        self.assertEqual(filter_transactions_by_currency(transactions), expected_transactions)

    def test_format_transaction_json(self):
        transaction = {
            "date": "2023-04-01T12:00:00Z",
            "operationAmount": {"amount": 1000, "currency": {"code": "RUB"}},
            "from": "Счет 1234",
            "to": "Счет 5678",
            "description": "Перевод",
        }
        expected_formatted_transaction = "01.04.2023 Перевод\nСчет 1234\nСчет 5678\nСумма: 1000 RUB\n\n"
        self.assertEqual(format_transaction(transaction), expected_formatted_transaction)

    def test_format_transaction_csv(self):
        transaction = {
            "date": "2023-04-01T12:00:00Z",
            "amount": 1500,
            "currency_code": "USD",
            "from": "Visa Platinum 1234 5678 9012",
            "to": "Счет 9876",
            "description": "Покупка",
        }
        expected_formatted_transaction = (
            "01.04.2023 Покупка\nVisa Platinum 1234 5678 9012\nСчет 9876\nСумма: 1500 USD\n\n"
        )
        self.assertEqual(format_transaction(transaction), expected_formatted_transaction)


if __name__ == "__main__":
    unittest.main()
