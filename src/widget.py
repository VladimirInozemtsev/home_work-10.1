from src import masks


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
        masked_number = masks.get_mask_card_number(data.split()[-1])
        masks.get_mask_card_number(data.split()[-1])
        return data.split()[0] + " " + masked_number
    elif "Счет" in data:
        # Маскировка номера счета
        masked_number = masks.get_mask_account(data.split()[-1])
        return data.split()[0] + " " + masked_number
    else:
        return "Неверный формат данных"


def get_date(date_string: str) -> str:
    """
    Функция принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").

    Args:
        date_string: Строка с датой в формате "2024-03-11T02:26:18.671407".

    Returns:
        Строка с датой в формате "ДД.ММ.ГГГГ".
    """
    year = date_string[:4]
    month = date_string[5:7]
    day = date_string[8:10]
    return f"{day}.{month}.{year}"
