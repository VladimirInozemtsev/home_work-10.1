import unittest
from src.filter_transactions import filter_transactions_by_description, count_transactions_by_category

class TestFilterTransactions(unittest.TestCase):

    def test_filter_transactions_by_description(self):
        transactions = [
            {'description': 'Перевод на карту'},
            {'description': 'Открытие вклада'},
            {'description': 'Перевод организации'}
        ]
        expected_transactions = [
            {'description': 'Перевод на карту'},
            {'description': 'Перевод организации'}
        ]
        self.assertEqual(filter_transactions_by_description(transactions, 'Перевод'), expected_transactions)

        # Проверка без учета регистра
        self.assertEqual(filter_transactions_by_description(transactions, 'перевод'), expected_transactions)

        # Проверка отсутствия совпадений
        self.assertEqual(filter_transactions_by_description(transactions, 'Покупка'), [])


if __name__ == '__main__':
    unittest.main()