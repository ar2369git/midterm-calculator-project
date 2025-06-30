import pytest
from app.history import HistoryManager
from app.calculation import Calculation

def test_undo_redo_empty():
    hm = HistoryManager(max_size=3)
    assert hm.undo() is None
    assert hm.redo() is None

def test_add_and_undo_redo():
    hm = HistoryManager(max_size=2)
    c1 = Calculation("add", 1, 2, 3)
    c2 = Calculation("sub", 5, 3, 2)
    hm.add(c1)
    hm.add(c2)
    assert hm.all == [c1, c2]

    u = hm.undo()
    assert u == c2
    assert hm.all == [c1]

    r = hm.redo()
    assert r == c2
    assert hm.all == [c1, c2]

def test_max_history_enforced():
    hm = HistoryManager(max_size=2)
    c1 = Calculation("a", 1, 1, 2)
    c2 = Calculation("b", 2, 2, 4)
    c3 = Calculation("c", 3, 3, 9)
    hm.add(c1)
    hm.add(c2)
    hm.add(c3)
    # oldest entry dropped
    assert hm.all == [c2, c3]

def test_snapshot_and_restore():
    hm = HistoryManager(max_size=5)
    c1 = Calculation("x", 1, 1, 2)
    c2 = Calculation("y", 2, 2, 4)
    hm.add(c1)
    hm.add(c2)
    m = hm.snapshot()

    # modify after snapshot
    c3 = Calculation("z", 3, 3, 9)
    hm.add(c3)
    assert len(hm.all) == 3

    # restore to snapshot
    hm.restore(m)
    assert hm.all == [c1, c2]
