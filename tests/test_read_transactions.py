import unittest
from unittest.mock import patch, MagicMock
import io
from src.read_transactions import read_transactions_from_csv, read_transactions_from_excel


class TestReadTransactions(unittest.TestCase):

    @patch("openpyxl.load_workbook", new_callable=MagicMock)
    def test_read_transactions_from_excel(self, mock_load_workbook):
        mock_workbook = MagicMock()
        mock_worksheet = MagicMock()
        mock_workbook.active = mock_worksheet
        mock_worksheet.iter_rows.return_value = [
            (
                "650703",
                "EXECUTED",
                "2023-09-05T11:30:32Z",
                "16210",
                "Sol",
                "PEN",
                "Счет 58803664561298323391",
                "Счет 39745660563456619397",
                "Перевод организации",
            )
        ]
        mock_load_workbook.return_value = mock_workbook

        transactions = read_transactions_from_excel("transactions_excel.xlsx")

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["id"], "650703")
        self.assertEqual(transactions[0]["state"], "EXECUTED")
        self.assertEqual(transactions[0]["date"], "2023-09-05T11:30:32Z")
        self.assertEqual(transactions[0]["amount"], "16210")
        self.assertEqual(transactions[0]["currency_name"], "Sol")
        self.assertEqual(transactions[0]["currency_code"], "PEN")
        self.assertEqual(transactions[0]["from"], "Счет 58803664561298323391")
        self.assertEqual(transactions[0]["to"], "Счет 39745660563456619397")
        self.assertEqual(transactions[0]["description"], "Перевод организации")


if __name__ == "__main__":
    unittest.main()
