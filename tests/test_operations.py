import pytest
from app.operations import OperationFactory, OperationError

@pytest.mark.parametrize("name,a,b,expected", [
    ("add", 2, 3, 5),
    ("subtract", 5, 2, 3),
    ("multiply", 3, 4, 12),
    ("divide", 10, 2, 5),
    ("power", 2, 3, 8),
    ("root", 27, 3, 3),
    ("modulus", 7, 4, 3),
    ("int_divide", 7, 4, 1),
    ("percent", 50, 200, 25),
    ("abs_diff", 5, 9, 4),
])
def test_ops(name, a, b, expected):
    op = OperationFactory.get(name)
    assert op.execute(a, b) == expected

def test_divide_zero():
    with pytest.raises(OperationError):
        OperationFactory.get("divide").execute(1, 0)
