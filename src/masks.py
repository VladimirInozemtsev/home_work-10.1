def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.

    Args:
        card_number: Номер карты.

    Returns:
        Маскированный номер карты в формате XXXX XX** **** XXXX.
    """

    if len(card_number) != 16:
        raise ValueError("Номер карты должен быть 16-значным.")

    masked_card_number = card_number[:4] + " " + card_number[4:6] + "**" + " " + "*" * 4 + " " + card_number[-4:]
    return masked_card_number


# card_number = "1234567890123456"
# print(get_mask_card_number(card_number))


def get_mask_account(account_number: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.

    Args:
        account_number: Номер счета.

    Returns:
        Маскированный номер счета в формате **XXXX.
    """

    if len(account_number) < 6:
        raise ValueError("Номер счета должен быть минимум 6-значным.")

    masked_account = "**" + account_number[-4:]
    return masked_account
