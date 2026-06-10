import pytest
from calculator import add, subtract, multiply, divide, calculate, main


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_calculate_success():
    assert calculate("add", 2, 3) == 5
    assert calculate("subtract", 5, 3) == 2
    assert calculate("multiply", 4, 3) == 12
    assert calculate("divide", 10, 2) == 5


def test_calculate_uppercase_operation():
    assert calculate("ADD", 2, 3) == 5


def test_calculate_invalid_operation():
    with pytest.raises(ValueError):
        calculate("bad", 2, 3)


def test_main_quit_immediately(monkeypatch, capsys):
    inputs = iter(["quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()

    captured = capsys.readouterr()
    assert "Python Calculator" in captured.out
    assert "Goodbye!" in captured.out


def test_main_successful_calculation(monkeypatch, capsys):
    inputs = iter(["add", "2", "3", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()

    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out
    assert "Goodbye!" in captured.out


def test_main_invalid_number_input(monkeypatch, capsys):
    inputs = iter(["add", "abc", "add", "2", "3", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()

    captured = capsys.readouterr()
    assert "Error:" in captured.out
    assert "Result: 5.0" in captured.out
    assert "Goodbye!" in captured.out


def test_main_divide_by_zero(monkeypatch, capsys):
    inputs = iter(["divide", "10", "0", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()

    captured = capsys.readouterr()
    assert "Cannot divide by zero" in captured.out
    assert "Goodbye!" in captured.out

    def test_main_guard_exists():
        assert main is not None