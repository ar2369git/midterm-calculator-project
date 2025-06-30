from app.calculation import Calculation

def test_calculation_record():
    c = Calculation("add", 1, 2, 3)
    assert c.op_name == "add"
    assert c.operands == (1, 2)
    assert c.result == 3
