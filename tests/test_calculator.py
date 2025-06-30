import pandas as pd
import pytest
from app.calculator import Calculator
from app.calculator_config import Config

@pytest.fixture(autouse=True)
def clean_env(tmp_path, monkeypatch):
    monkeypatch.setenv("CALCULATOR_HISTORY_DIR", str(tmp_path))
    return tmp_path

def test_save_load(clean_env):
    calc = Calculator()
    calc._perform("add", "2", "3")
    calc.save_history()
    file = clean_env / Config.HISTORY_FILE
    assert file.exists()
    df = pd.read_csv(file)
    assert df.iloc[0]["operation"] == "add"
