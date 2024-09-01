import unittest, requests
from unittest.mock import patch
from src.external_api import get_currency_rate, convert_amount_to_rub


class TestExternalAPI(unittest.TestCase):

    @patch("external_api.requests.get")
    def test_get_currency_rate_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"rates": {"RUB": 75.0}}

        rate = get_currency_rate("USD", "RUB")
        self.assertEqual(rate, 75.0)

    @patch("external_api.requests.get")
    def test_get_currency_rate_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Ошибка запроса")
        with self.assertRaises(ExternalAPIError):
            get_currency_rate("USD", "RUB")

    @patch("external_api.get_currency_rate")
    def test_convert_amount_to_rub_usd(self, mock_get_currency_rate):
        mock_get_currency_rate.return_value = 75.0
        transaction = {"amount": "100", "currency": "USD"}
        amount_rub = convert_amount_to_rub(transaction)
        self.assertEqual(amount_rub, 7500.0)

    @patch("external_api.get_currency_rate")
    def test_convert_amount_to_rub_eur(self, mock_get_currency_rate):
        mock_get_currency_rate.return_value = 90.0
        transaction = {"amount": "50", "currency": "EUR"}
        amount_rub = convert_amount_to_rub(transaction)
        self.assertEqual(amount_rub, 4500.0)

    def test_convert_amount_to_rub_rub(self):
        transaction = {"amount": "1000", "currency": "RUB"}
        amount_rub = convert_amount_to_rub(transaction)
        self.assertEqual(amount_rub, 1000.0)

    def test_convert_amount_to_rub_unsupported_currency(self):
        transaction = {"amount": "100", "currency": "JPY"}
        amount_rub = convert_amount_to_rub(transaction)
        self.assertIsNone(amount_rub)

    @patch("external_api.get_currency_rate")
    def test_convert_amount_to_rub_api_error(self, mock_get_currency_rate):
        mock_get_currency_rate.side_effect = ExternalAPIError("Ошибка API")
        transaction = {"amount": "100", "currency": "USD"}
        amount_rub = convert_amount_to_rub(transaction)
        self.assertIsNone(amount_rub)


#if __name__ == "__main__":
   # unittest.main()
