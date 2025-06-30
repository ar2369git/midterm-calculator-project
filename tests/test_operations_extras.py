import pytest
from app.operations import OperationFactory, OperationError

@pytest.mark.parametrize("name,a,b", [
    ("root", 2, 0),
    ("modulus", 1, 0),
    ("int_divide", 1, 0),
    ("percent", 1, 0),
])
def test_operations_raise_on_invalid_inputs(name, a, b):
    op = OperationFactory.get(name)
    with pytest.raises(OperationError):
        op.execute(a, b)

def test_unknown_operation_name():
    with pytest.raises(OperationError):
        OperationFactory.get("unknown_op")
