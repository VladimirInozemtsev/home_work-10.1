import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected_masked_number ",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("1234567890123789", "1234 56** **** 3789"),
        ("9547896214578963", "9547 89** **** 8963"),
    ],
)
def test_mask_card_number_valid(card_number, expected_masked_number):
    assert get_mask_card_number(card_number) == expected_masked_number


def test_mask_card_number_valid_(mask_card_number):
    assert get_mask_card_number(mask_card_number) == "1234 56** **** 3456"


@pytest.mark.parametrize("card_number, expected", [("12345", ValueError), ("", ValueError), ("0", ValueError)])
def test_mask_card_number_invalid_input(card_number, expected):
    with pytest.raises(expected):
        get_mask_card_number(card_number)


def test_mask_account_valid(account_number):
    assert get_mask_account(account_number) == "**3456"


@pytest.mark.parametrize(
    "account_number, expected_error", [("12345", ValueError), ("", ValueError), ("0", ValueError)]
)
def test_mask_account_invalid_input(account_number, expected_error):
    with pytest.raises(expected_error):
        get_mask_account(account_number)
