# test_main.py

from main import add

def test_add():
    assert add(2, 3) == 5         # simple case
    assert add(-1, 1) == 0        # edge case (positive + negative)
    assert add(0, 0) == 0         # zero case
