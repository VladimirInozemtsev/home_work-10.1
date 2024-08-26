import pytest
from src.decorators import my_function, my_function_2, log


def test_log_success(capsys):
    """Проверяет логирование успешного выполнения функции."""
    my_function(1, 2)
    captured = capsys.readouterr()
    assert "my_function started" in captured.out
    assert "my_function ok" in captured.out


def test_log_error(capsys):
    """Проверяет логирование ошибки."""
    with pytest.raises(ZeroDivisionError):
        my_function_2(1, 0)
    captured = capsys.readouterr()
    assert "my_function_2 started" in captured.out
    assert "my_function_2 error: <class 'ZeroDivisionError'>" in captured.out
    assert "(1, 0)" in captured.out
