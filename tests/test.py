def get_mask_card_number(card_number):
    """
    Функция принимает на вход номер карты и возвращает ее маску.

    Args:
        card_number: Номер карты.

    Returns:
        Маскированный номер карты в формате XXXX XX** **** XXXX.
    """

    masked_card_number = card_number[:4] + " " + card_number[4:6] + "**" + " " + "*" * 4 + " " + card_number[-4:]
    return masked_card_number


# Пример использования
# card_number = "7000792289606361"
# masked_card_number = get_mask_card_number(card_number)
# print(masked_card_number)


def get_mask_account(account_number):
    """
    Функция принимает на вход номер счета и возвращает его маску.

    Args:
        account_number: Номер счета.

    Returns:
        Маскированный номер счета в формате **XXXX.
    """

    masked_account = "**" + account_number[-4:]
    return masked_account


# Пример использования
# account_number = "73654108430135874305"
# masked_account = get_mask_account(account_number)
# # print(masked_account)  # Вывод: **4305
