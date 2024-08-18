from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(data: str) -> str:
    """
    Функция принимает на вход строку, содержащую тип и номер карты или счета,
    и возвращает строку с замаскированным номером.
    Args:
        data: Строка с типом и номером карты или счета.

    Returns:
        Строка с замаскированным номером.
    """

    if "Visa" in data or "Maestro" in data:
        # Маскировка номера карты
        masked_number = get_mask_card_number(data.split()[-1])
        get_mask_card_number(data.split()[-1])
        return data.split()[0] + " " + masked_number
    elif "Счет" in data:
        # Маскировка номера счета
        masked_number = get_mask_account(data.split()[-1])
        return data.split()[0] + " " + masked_number
    else:
        return "Неверный формат данных"


# print(mask_account_card("Visa Platinum 7000792289606361"))  # Вывод: Visa Platinum 7000 7922 ** **** 6361
# print(mask_account_card("Maestro 7000792289606361"))  # Вывод: Maestro 7000 7922 ** **** 6361
# print(mask_account_card("Счет 73654108430135874305"))  # Вывод: Счет **4305
# print(mask_account_card("Неверный формат 1234567890"))  # Вывод: Неверный формат данных


def get_date(date_string: str) -> str:
    """
    Функция принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").

    Args:
        date_string: Строка с датой в формате "2024-03-11T02:26:18.671407".

    Returns:
        Строка с датой в формате "ДД.ММ.ГГГГ".
    """
    try:
        year = date_string[:4]
        month = date_string[5:7]
        day = date_string[8:10]
        # Проверка, что все части даты являются цифрами
        if not year.isdigit() or not month.isdigit() or not day.isdigit():
            raise ValueError("Некорректный формат даты")
        return f"{day}.{month}.{year}"
    except IndexError:
        raise ValueError("Некорректный формат даты")
    except ValueError:
        raise ValueError("Некорректный формат даты")


# print(get_date("Some text"))
