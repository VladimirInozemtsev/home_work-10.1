import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные окружения из .env


class ExternalAPIError(Exception):
    """
    Исключение, которое возникает при ошибке обращения к внешнему API.
    """

    pass


def get_currency_rate(from_currency, to_currency, amount):
    """
    Получает курс валюты с помощью Exchange Rates Data API.

    Args:
        from_currency: Базовая валюта.
        to_currency: Целевая валюта.
        amount: Сумма, которую нужно конвертировать.

    Returns:
        Курс валюты.
    """

    api_key = os.getenv("EXCHANGE_RATES_API_KEY")
    url = "https://api.apilayer.com/exchangerates_data/convert"

    # Передаем параметры в виде keyword arguments
    response = requests.get(
        url, headers={"apikey": api_key}, params={"to": to_currency, "from": from_currency, "amount": amount}
    )
    response.raise_for_status()  # Проверка на ошибки HTTP
    data = response.json()
    return data["result"]


def convert_amount_to_rub(transaction):
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction: Словарь с данными о транзакции.

    Returns:
        Сумма транзакции в рублях.
    """

    amount = transaction["amount"]
    currency = transaction["currency"]

    if currency == "RUB":
        return float(amount)
    elif currency in ("USD", "EUR"):
        try:
            result = get_currency_rate(currency, "RUB")
            return round(result, 2)
        except ExternalAPIError as e:
            print(f"Ошибка конвертации: {e}")
            return None  # Возвращаем None в случае ошибки
    else:
        return None  # Возвращаем None для неподдерживаемых валют
