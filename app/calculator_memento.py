class Memento:
    def __init__(self, history, redo_stack):
        # store deep-copies of the two stacks
        self._state = (list(history), list(redo_stack))
    def get_state(self):
        return [list(self._state[0]), list(self._state[1])]
