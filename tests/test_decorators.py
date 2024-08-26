import pytest
from src.decorators import my_function, my_function_2, log


def test_log_with_filename(tmpdir):
    """Проверяет логирование в файл."""
    log_file = tmpdir.join("mylog.txt")
    log_file.write("")  # Создаем пустой файл

    @log(filename=str(log_file))
    def my_function_3(x, y):
        return x + y

    my_function_3(1, 2)
    with open(str(log_file), "r") as f:
        content = f.read()
        assert "my_function_3 started" in content
        assert "my_function_3 ok" in content


def test_log_error(capsys):
    """Проверяет логирование ошибки."""
    with pytest.raises(ZeroDivisionError):
        my_function_2(1, 0)
    captured = capsys.readouterr()
    assert "my_function_2 started" in captured.out
    assert "my_function_2 error: <class 'ZeroDivisionError'>" in captured.out
    assert "(1, 0)" in captured.out


