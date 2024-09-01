def log(filename: str = None):
    """
    Декоратор, который логирует начало и конец выполнения функции, а также ее результаты
    или возникшие ошибки.

    Args:
        filename: Имя файла для записи логов. Если не задан, логи выводятся в консоль.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            if filename:
                with open(filename, "a") as f:  # Открываем файл в режиме добавления
                    f.write(f"{func.__name__} started\n")
                    try:
                        result = func(*args, **kwargs)
                        f.write(f"{func.__name__} ok\n")
                        return result
                    except Exception as e:
                        f.write(f"{func.__name__} error: {type(e)}. Inputs: {args}, {kwargs}\n")
                        raise
            else:
                print(f"{func.__name__} started")
                try:
                    result = func(*args, **kwargs)
                    print(f"{func.__name__} ok")
                    return result
                except Exception as e:
                    print(f"{func.__name__} error: {type(e)}. Inputs: {args}, {kwargs}")
                    raise
        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


@log()
def my_function_2(x, y):
    return x / y


my_function(4, 2)
