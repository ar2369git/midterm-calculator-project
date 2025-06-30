import os
import pandas as pd
from colorama import init, Fore, Style

from .calculator_config import Config
from .input_validators import validate_number
from .operations import OperationFactory
from .history import HistoryManager
from .calculation import Calculation
from .logger import logger

init(autoreset=True)

class Calculator:
    def __init__(self):
        # allow tests (and users) to override the history dir via ENV
        history_dir = os.getenv("CALCULATOR_HISTORY_DIR", Config.HISTORY_DIR)
        os.makedirs(history_dir, exist_ok=True)
        self._history_dir = history_dir
        self.history = HistoryManager(Config.MAX_HISTORY)

    def _perform(self, op_name, a, b):
        a, b = validate_number(a), validate_number(b)
        op = OperationFactory.get(op_name)
        result = round(op.execute(a, b), Config.PRECISION)
        calc = Calculation(op_name, a, b, result)
        self.history.add(calc)
        logger.info(f"{op_name} {a} {b} = {result}")
        if Config.AUTO_SAVE:
            self.save_history()
        return calc

    def save_history(self):
        df = pd.DataFrame([{
            "timestamp": c.timestamp,
            "operation": c.op_name,
            "a": c.operands[0],
            "b": c.operands[1],
            "result": c.result
        } for c in self.history.all])
        out = os.path.join(self._history_dir, Config.HISTORY_FILE)
        df.to_csv(out, index=False, encoding=Config.ENCODING)

    def load_history(self):
        path = os.path.join(self._history_dir, Config.HISTORY_FILE)
        if not os.path.exists(path):
            print("No history file found.")
            return
        df = pd.read_csv(path, encoding=Config.ENCODING)
        self.history = HistoryManager(Config.MAX_HISTORY)
        for _, row in df.iterrows():
            self.history.add(Calculation(
                row.operation, row.a, row.b, row.result
            ))

    def repl(self):
        print(Fore.GREEN + "Calculator REPL. Type 'help' for commands.")
        while True:
            cmd, *args = input(">> ").strip().split()
            try:
                if cmd in OperationFactory._map:
                    calc = self._perform(cmd, *args)
                    print(f"= {calc.result}")
                elif cmd == "history":
                    for c in self.history.all:
                        print(c.timestamp, c.op_name, c.operands, c.result)
                elif cmd == "clear":
                    self.history = HistoryManager(Config.MAX_HISTORY)
                    print("History cleared.")
                elif cmd == "undo":
                    u = self.history.undo()
                    print("Undone:", u.result if u else "Nothing to undo")
                elif cmd == "redo":
                    r = self.history.redo()
                    print("Redone:", r.result if r else "Nothing to redo")
                elif cmd == "save":
                    self.save_history()
                    print("History saved.")
                elif cmd == "load":
                    self.load_history()
                elif cmd == "help":
                    print(", ".join(
                        list(OperationFactory._map) +
                        ["history", "clear", "undo", "redo", "save", "load", "exit"]
                    ))
                elif cmd == "exit":
                    break
                else:
                    print("Unknown command. Type 'help'.")
            except Exception as e:
                logger.error(str(e))
                print(Fore.RED + f"Error: {e}")

if __name__ == "__main__":
    Calculator().repl()
