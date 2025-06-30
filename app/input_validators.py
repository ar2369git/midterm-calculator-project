from .exceptions import ValidationError
from .calculator_config import Config

def validate_number(x):
    try:
        v = float(x)
    except ValueError:
        raise ValidationError(f"Invalid number: {x}")
    if abs(v) > Config.MAX_INPUT:
        raise ValidationError(f"Input {v} exceeds max allowed {Config.MAX_INPUT}")
    return v
