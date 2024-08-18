import pytest
from src.widget import mask_account_card
from src.widget import get_date


@pytest.mark.parametrize(
    "data, expected",
    (
        ["Visa 7000792289606361", "Visa 7000 79** **** 6361"],
        ["Maestro 7000792289606361", "Maestro 7000 79** **** 6361"],
        ["Счет 73654108430135874305", "Счет **4305"],
    ),
)
def test_mask_account_card(data: str, expected: str) -> str:
    assert mask_account_card(data) == expected


@pytest.mark.parametrize(
    "data, expected_masked_data",
    [
        ("Мир 1234567890123456", "Неверный формат данных"),
        ("Неизвестный тип 1234567890123456", "Неверный формат данных"),
        ("", "Неверный формат данных"),
    ],
)
def test_mask_account_card_invalid(data, expected_masked_data):
    assert mask_account_card(data) == expected_masked_data


@pytest.mark.parametrize(
    "date_string, expected_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-31T23:59:59.999999", "31.12.2023"),
        ("1999-01-01T00:00:00.000000", "01.01.1999"),
    ],
)
def test_get_date_valid(date_string, expected_date):
    assert get_date(date_string) == expected_date


@pytest.mark.parametrize(
    "date_string",
    [
        "",
        " ",
        "Some text",
    ],
)
def test_get_date_invalid_format(date_string):
    with pytest.raises(ValueError):
        get_date(date_string)
