from abc import ABC, abstractmethod
from .exceptions import OperationError

class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class Add(Operation):
    def execute(self, a, b): return a + b

class Subtract(Operation):
    def execute(self, a, b): return a - b

class Multiply(Operation):
    def execute(self, a, b): return a * b

class Divide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Division by zero")
        return a / b

class Power(Operation):
    def execute(self, a, b): return a ** b

class Root(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Root degree zero")
        return a ** (1.0 / b)

class Modulus(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Modulus by zero")
        return a % b

class IntDivide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Integer division by zero")
        return a // b

class Percentage(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Percentage base zero")
        return (a / b) * 100

class AbsDiff(Operation):
    def execute(self, a, b): return abs(a - b)

class OperationFactory:
    _map = {
        "add": Add,
        "subtract": Subtract,
        "multiply": Multiply,
        "divide": Divide,
        "power": Power,
        "root": Root,
        "modulus": Modulus,
        "int_divide": IntDivide,
        "percent": Percentage,
        "abs_diff": AbsDiff
    }

    @classmethod
    def get(cls, name):
        op_cls = cls._map.get(name)
        if not op_cls:
            raise OperationError(f"Unknown operation '{name}'")
        return op_cls()
