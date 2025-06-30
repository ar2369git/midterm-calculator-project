import pytest, pandas as pd
from app.calculator import Calculator
from app.calculator_config import Config
from app.exceptions import ValidationError, OperationError


def test_perform_invalid_and_zero_div(monkeypatch):
    # disable autosave for clean test behavior
    monkeypatch.setenv("CALCULATOR_AUTO_SAVE", "false")
    # also update runtime flag
    monkeypatch.setattr(Config, "AUTO_SAVE", False)

    calc = Calculator()
    with pytest.raises(ValidationError):
        calc._perform("add", "abc", "1")
    with pytest.raises(OperationError):
        calc._perform("divide", "1", "0")


def test_load_no_history(tmp_path, monkeypatch, capsys):
    # override history dir to an empty temp path
    monkeypatch.setenv("CALCULATOR_HISTORY_DIR", str(tmp_path))

    calc = Calculator()
    calc.load_history()
    out = capsys.readouterr().out
    assert "No history file found." in out


def test_repl_full_flow(monkeypatch, capsys):
    # disable autosave in _perform
    monkeypatch.setenv("CALCULATOR_AUTO_SAVE", "false")
    monkeypatch.setattr(Config, "AUTO_SAVE", False)

    # import Calculator after Config override
    from app.calculator import Calculator

    # stub out save and load to avoid file operations
    monkeypatch.setattr(Calculator, "save_history", lambda self: print("SAVE_CALLED"))
    monkeypatch.setattr(Calculator, "load_history", lambda self: print("LOAD_CALLED"))

    # simulate user input sequence
    commands = [
        "add 10 5",
        "subtract 8 3",
        "history",
        "undo",
        "redo",
        "clear",
        "save",
        "load",
        "help",
        "foobar",
        "exit"
    ]
    inputs = iter(commands)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calc = Calculator()
    calc.repl()

    out = capsys.readouterr().out
    # verify major REPL outputs
    assert "= 15" in out
    assert "= 5" in out
    assert "Undone:" in out
    assert "Redone:" in out
    assert "History cleared." in out
    assert "SAVE_CALLED" in out
    assert "History saved." in out
    assert "LOAD_CALLED" in out
    assert "add, subtract" in out
    assert "Unknown command. Type 'help'." in out
