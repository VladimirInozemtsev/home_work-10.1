import unittest
import json
from src.utils import read_transactions_from_json

class TestReadTransactionsFromJson(unittest.TestCase):

    def test_read_valid_json(self):
        """Проверяет чтение корректного JSON-файла."""
        filepath = "test_transactions.json"
        with open(filepath, "w") as file:
            json.dump([
                {"amount": 100, "currency": "USD"},
                {"amount": 50, "currency": "EUR"}
            ], file)

        transactions = read_transactions_from_json(filepath)
        self.assertEqual(len(transactions), 2)
        self.assertEqual(transactions[0]["amount"], 100)
        self.assertEqual(transactions[0]["currency"], "USD")
        self.assertEqual(transactions[1]["amount"], 50)
        self.assertEqual(transactions[1]["currency"], "EUR")

    def test_read_empty_file(self):
        """Проверяет чтение пустого JSON-файла."""
        filepath = "empty_transactions.json"
        with open(filepath, "w") as file:
            pass  # Создаем пустой файл

        transactions = read_transactions_from_json(filepath)
        self.assertEqual(transactions, [])

    def test_read_invalid_json(self):
        """Проверяет чтение файла с некорректным JSON."""
        filepath = "invalid_transactions.json"
        with open(filepath, "w") as file:
            file.write("This is not valid JSON")

        transactions = read_transactions_from_json(filepath)
        self.assertEqual(transactions, [])

    def test_read_non_list_json(self):
        """Проверяет чтение JSON-файла, содержащего не список."""
        filepath = "non_list_transactions.json"
        with open(filepath, "w") as file:
            json.dump({"amount": 100, "currency": "USD"}, file)

        transactions = read_transactions_from_json(filepath)
        self.assertEqual(transactions, [])

    def test_read_nonexistent_file(self):
        """Проверяет чтение несуществующего файла."""
        filepath = "nonexistent_transactions.json"
        transactions = read_transactions_from_json(filepath)
        self.assertEqual(transactions, [])

if __name__ == '__main__':
    unittest.main()