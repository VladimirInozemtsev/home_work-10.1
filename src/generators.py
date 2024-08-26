def filter_by_currency(transactions: list, currency: str) -> iter:
    """
    Функция принимает на вход список словарей, представляющих транзакции,
    и строку с кодом валюты.
    Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции
    соответствует заданной.

    Args:
        transactions: Список словарей, представляющих транзакции.
        currency: Строка с кодом валюты.

    Returns:
        Итератор, выдающий транзакции с заданной валютой.
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list) -> iter:
    """
    Генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди.

    Args:
        transactions: Список словарей с транзакциями.

    Yields:
        Описание операции в виде строки.
    """

    for transaction in transactions:
        description = transaction.get("description", "Описание операции отсутствует")
        yield description


def card_number_generator(start: int, end: int) -> iter:
    """
    Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты. Генератор может сгенерировать номера карт
    в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.

    Args:
        start: Начальное значение для генерации диапазона номеров.
        end: Конечное значение для генерации диапазона номеров.

    Yields:
        Номер банковской карты в формате XXXX XXXX XXXX XXXX.
    """
    for i in range(start, end + 1):
        card_number = f"{i:016}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"


# for card_number in card_number_generator(1, 999):
# print(card_number)
