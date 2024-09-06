import unittest
import os
import requests
from dotenv import load_dotenv
from unittest.mock import patch, MagicMock
from src.external_api import get_currency_rate, convert_amount_to_rub, ExternalAPIError

load_dotenv()  # Загружаем переменные окружения из .env

class TestCurrencyConverter(unittest.TestCase):

    @patch('requests.get')
    def test_get_currency_rate_success(self, mock_get):
        # Имитация успешного ответа API
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'result': 75.5}
        mock_get.return_value = mock_response

        # Тест с действительными валютными кодами
        result = get_currency_rate("USD", "RUB", 1)
        self.assertEqual(result, 75.5)

    @patch('requests.get')
    def test_get_currency_rate_api_error(self, mock_get):
        # Имитация ошибки API
        mock_get.side_effect = requests.exceptions.RequestException("API Error")

        with self.assertRaises(ExternalAPIError) as context:
            get_currency_rate("USD", "RUB", 1)

        self.assertEqual(str(context.exception), "Ошибка запроса к API: API Error")

    def test_convert_amount_to_rub_rub(self):
        transaction = {"amount": 100, "currency": "RUB"}
        result = convert_amount_to_rub(transaction)
        self.assertEqual(result, 100.0)

    @patch('src.external_api.get_currency_rate')
    def test_convert_amount_to_rub_usd(self, mock_get_currency_rate):
        # Имитация курса валюты для USD в RUB
        mock_get_currency_rate.return_value = 75.5

        transaction = {"amount": 100, "currency": "USD"}
        result = convert_amount_to_rub(transaction)
        self.assertEqual(result, 75.5)

    @patch('src.external_api.get_currency_rate')
    def test_convert_amount_to_rub_eur(self, mock_get_currency_rate):
        # Имитация курса валюты для EUR в RUB
        mock_get_currency_rate.return_value = 90.2

        transaction = {"amount": 100, "currency": "EUR"}
        result = convert_amount_to_rub(transaction)
        self.assertEqual(result, 90.2)

    @patch('src.external_api.get_currency_rate')
    def test_convert_amount_to_rub_api_error(self, mock_get_currency_rate):
        # Имитация ошибки API во время конвертации
        mock_get_currency_rate.side_effect = ExternalAPIError("API Error")

        transaction = {"amount": 100, "currency": "USD"}
        result = convert_amount_to_rub(transaction)
        self.assertIsNone(result)  # Проверка, возвращается ли None при ошибке

    def test_convert_amount_to_rub_unsupported_currency(self):
        transaction = {"amount": 100, "currency": "JPY"}
        result = convert_amount_to_rub(transaction)
        self.assertIsNone(result)  # Проверка, возвращается ли None для неподдерживаемых валют

if __name__ == '__main__':
    unittest.main()