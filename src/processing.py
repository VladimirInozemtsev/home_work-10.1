def filter_by_state(data: list, state: str = 'EXECUTED') -> list:
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
    if item['state'] == state:
      filtered_data.append(item)
  return filtered_data


# Словарь#
#data = [
  #{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
  #{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
  #{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
  #{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
#]

# Выход функции со статусом по умолчанию 'EXECUTED'
# print(filter_by_state(data))  # Вывод: [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Выход функции, если вторым аргументом передано 'CANCELED'
# print(filter_by_state(data, 'CANCELED')) # Вывод: [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


