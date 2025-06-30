from .calculator_memento import Memento
from .calculation import Calculation

class HistoryManager:
    def __init__(self, max_size):
        self._history = []
        self._redo_stack = []
        self._max = max_size

    def add(self, calc: Calculation):
        self._redo_stack.clear()
        self._history.append(calc)
        if len(self._history) > self._max:
            self._history.pop(0)

    def undo(self):
        if not self._history:
            return None
        calc = self._history.pop()
        self._redo_stack.append(calc)
        return calc

    def redo(self):
        if not self._redo_stack:
            return None
        calc = self._redo_stack.pop()
        self._history.append(calc)
        return calc

    def snapshot(self):
        return Memento(self._history, self._redo_stack)

    def restore(self, memento: Memento):
        hist, redo = memento.get_state()
        self._history, self._redo_stack = hist, redo

    @property
    def all(self):
        return list(self._history)
