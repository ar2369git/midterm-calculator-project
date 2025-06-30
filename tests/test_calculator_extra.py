import pandas as pd
from app.calculator import Calculator
from app.calculator_config import Config

def test_load_history(tmp_path, monkeypatch):
    # prepare a fake history CSV
    data = {
        "timestamp": ["2020-01-01T00:00:00"],
        "operation": ["add"],
        "a": [1],
        "b": [2],
        "result": [3],
    }
    df = pd.DataFrame(data)
    history_file = tmp_path / Config.HISTORY_FILE
    df.to_csv(history_file, index=False)

    # point Calculator at our tmp folder
    monkeypatch.setenv("CALCULATOR_HISTORY_DIR", str(tmp_path))

    calc = Calculator()
    calc.load_history()
    hist = calc.history.all

    assert len(hist) == 1
    c = hist[0]
    assert c.op_name == "add"
    assert c.operands == (1, 2)
    assert c.result == 3
