from datetime import datetime

class Calculation:
    def __init__(self, op_name, a, b, result):
        self.timestamp = datetime.utcnow()
        self.op_name = op_name
        self.operands = (a, b)
        self.result = result
