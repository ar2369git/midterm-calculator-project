import pytest
from app.input_validators import validate_number
from app.exceptions import ValidationError
from app.calculator_config import Config

def test_validate_number_valid():
    assert validate_number("123") == 123.0
    assert validate_number("-45.6") == -45.6

def test_validate_number_invalid_string():
    with pytest.raises(ValidationError):
        validate_number("not_a_number")

def test_validate_number_exceeds_max(monkeypatch):
    # temporarily lower the max allowed
    monkeypatch.setattr(Config, "MAX_INPUT", 10)
    with pytest.raises(ValidationError):
        validate_number("20")
