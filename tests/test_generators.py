import pytest
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency, expected_results",
    [
        (
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
        ),
        (
            "EUR",
            [
                {
                    "id": 1642325595,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "21074.93", "currency": {"name": "EUR", "code": "EUR"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
        ),
    ],
)
def test_filter_by_currency(transactions: list[dict], currency: str, expected_results: list[dict]):
    filtered_transactions = list(filter_by_currency(transactions, currency))
    assert filtered_transactions == expected_results


@pytest.mark.parametrize(
    "transactions, expected_descriptions",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
            ["Перевод организации", "Перевод со счета на счет"],
        ),
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
            ],
            ["Описание операции отсутствует"],
        ),
        (
            [],
            [],
        ),
    ],
)
def test_transaction_descriptions(transactions: list[dict], expected_descriptions: list[str]):
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == expected_descriptions


@pytest.mark.parametrize(
    "start, end, expected_numbers",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]),
        (1000, 1002, ["0000 0000 0000 1000", "0000 0000 0000 1001", "0000 0000 0000 1002"]),
        (
            1000000000,
            1000000003,
            ["0000 0010 0000 0000", "0000 0010 0000 0001", "0000 0010 0000 0002", "0000 0010 0000 0003"],
        ),
    ],
)
def test_card_number_generator(start: int, end: int, expected_numbers: list[str]):
    generated_numbers = list(card_number_generator(start, end))
    assert generated_numbers == expected_numbers


def test_card_number_generator_empty_range() -> list[str]:
    generated_numbers = list(card_number_generator(5, 4))
    assert generated_numbers == []


def test_card_number_generator_single_value() -> list[str]:
    generated_numbers = list(card_number_generator(10, 10))
    assert generated_numbers == ["0000 0000 0000 0010"]
