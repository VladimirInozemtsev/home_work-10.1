def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """
    Функция принимает список словарей и опционально значение для ключа 'state' (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ 'state'
    соответствует указанному значению.

    Args:
        data: Список словарей.
        state: Значение для ключа 'state'.

    Returns:
        Новый список словарей, содержащий только те словари, у которых ключ 'state' соответствует указанному значению.
    """

    filtered_data = []
    for item in data:
        if item["state"] == state:
            filtered_data.append(item)
    return filtered_data


def sort_by_date(data: list, reverse: bool = True) -> list:
    """
    Функция принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date).

    Args:
        data: Список словарей.
        reverse: Порядок сортировки (True — убывание, False — возрастание).

    Returns:
        Новый список, отсортированный по дате.
    """

    return sorted(data, key=lambda item: item["date"], reverse=reverse)
