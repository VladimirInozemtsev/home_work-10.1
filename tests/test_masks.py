import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account


def test_mask_card_number_valid():
    card_number = "1234567890123456"
    expected_masked_number = "1234 56** **** 3456"
    assert get_mask_card_number(card_number) == expected_masked_number


@pytest.mark.parametrize(
    "card_number, expected", [("12345", ValueError), ("", ValueError), ("12345678901234567", ValueError)]
)
def test_mask_card_number_invalid_input(card_number, expected):
    with pytest.raises(expected):
        get_mask_card_number(card_number)


def test_mask_account_valid():
    account_number = "123456"
    expected_masked_number = "**3456"
    assert get_mask_account(account_number) == expected_masked_number


@pytest.mark.parametrize(
    "account_number, expected_error", [("12345", ValueError), ("", ValueError), ("1234567", ValueError)]
)
def test_mask_account_invalid_input(account_number, expected_error):
    with pytest.raises(expected_error):
        get_mask_account(account_number)
