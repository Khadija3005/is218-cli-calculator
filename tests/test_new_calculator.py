import pytest
from calculator.operations import Operations
from calculator.calculation import Calculation, ArithmeticCalculation
from calculator.commands import CalculateCommand, HistoryCommand
from calculator.cli import main


@pytest.mark.parametrize("operation,a,b,expected", [
    (Operations.add, 5, 3, 8),
    (Operations.add, -2.5, 1.5, -1),
    (Operations.subtract, 5, 3, 2),
    (Operations.multiply, 5, 3, 15),
    (Operations.multiply, 0, 5, 0),
    (Operations.divide, 6, 3, 2),
    (Operations.divide, -5, 2, -2.5),
])
def test_operations(operation, a, b, expected):
    assert operation(a, b) == expected


def test_divide_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Operations.divide(5, 0)


def test_abstract_calculation():
    with pytest.raises(TypeError):
        Calculation(5, 3, Operations.add)


def test_factory():
    calc = ArithmeticCalculation.create(5, 3, Operations.add)
    assert isinstance(calc, ArithmeticCalculation)
    assert calc.a == 5
    assert calc.b == 3
    assert calc.operation is Operations.add
    assert calc.execute() == 8


@pytest.mark.parametrize("operation,expected", [
    (Operations.subtract, 2),
    (Operations.multiply, 15),
    (Operations.divide, 5 / 3),
])
def test_strategies(operation, expected):
    calc = ArithmeticCalculation.create(5, 3, operation)
    assert calc.execute() == expected


def test_command_history():
    history = []
    calc = ArithmeticCalculation.create(5, 3, Operations.add)
    command = CalculateCommand(calc, history)
    assert command.execute() == 8
    assert history == ["5 add 3 = 8"]


def test_failed_command():
    history = []
    calc = ArithmeticCalculation.create(5, 0, Operations.divide)
    with pytest.raises(ValueError):
        CalculateCommand(calc, history).execute()
    assert history == []


def test_history_copy():
    history = ["5 add 3 = 8"]
    result = HistoryCommand(history).execute()
    result.append("fake")
    assert history == ["5 add 3 = 8"]


def test_empty_history():
    assert HistoryCommand([]).execute() == []


def test_cli(monkeypatch, capsys):
    commands = iter([
        "",
        "help",
        "unknown",
        "add 5",
        "add 5 3 2",
        "add abc 3",
        "divide 5 0",
        "history",
        "add 5 3",
        "subtract 5 3",
        "multiply 5 3",
        "divide 6 3",
        "history",
        "exit",
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(commands))
    main()
    output = capsys.readouterr().out

    assert "Commands:" in output
    assert "Unknown command" in output
    assert "exactly two numbers" in output
    assert "could not convert" in output
    assert "Cannot divide by zero" in output
    assert "History is empty" in output
    assert "5 add 3 = 8" in output
    assert "15" in output
    assert "Goodbye!" in output


def test_eof(monkeypatch, capsys):
    def end_input(_):
        raise EOFError

    monkeypatch.setattr("builtins.input", end_input)
    main()
    assert "Goodbye!" in capsys.readouterr().out


def test_keyboard_interrupt(monkeypatch, capsys):
    def interrupt(_):
        raise KeyboardInterrupt

    monkeypatch.setattr("builtins.input", interrupt)
    main()
    assert "Goodbye!" in capsys.readouterr().out
