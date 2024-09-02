import unittest, json
from unittest.mock import patch
from src.utils import read_transactions_from_json


class TestUtils(unittest.TestCase):
    @patch("utils.open", create=True)
    def test_read_transactions_from_json_success(self, mock_open):
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = json.dumps(
            [{"amount": "100", "currency": "RUB"}, {"amount": "50", "currency": "USD"}]
        )
        filepath = "data/operations.json"
        transactions = read_transactions_from_json(filepath)
        self.assertEqual(len(transactions), 2)

    @patch("utils.open", create=True)
    def test_read_transactions_from_json_empty_file(self, mock_open):
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = ""
        filepath = "data/operations.json"
        transactions = read_transactions_from_json(filepath)
        self.assertEqual(transactions, [])

    @patch("utils.open", create=True)
    def test_read_transactions_from_json_invalid_json(self, mock_open):
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = "invalid json"
        filepath = "data/operations.json"
        transactions = read_transactions_from_json(filepath)
        self.assertEqual(transactions, [])

    @patch("utils.open", create=True)
    def test_read_transactions_from_json_not_list(self, mock_open):
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = json.dumps({"amount": "100", "currency": "RUB"})
        filepath = "data/operations.json"
        transactions = read_transactions_from_json(filepath)
        self.assertEqual(transactions, [])

    @patch("utils.open")
    def test_read_transactions_from_json_file_not_found(self, mock_open):
        mock_open.side_effect = FileNotFoundError
        filepath = "data/operations.json"
        transactions = read_transactions_from_json(filepath)
        self.assertEqual(transactions, [])


if __name__ == "__main__":
    unittest.main()
