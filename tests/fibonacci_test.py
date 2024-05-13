import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fibonacci import fib

def test_fib_0():
    assert fib(0) == 0

def test_fib_1():
    assert fib(1) == 1

def test_fib_10():
    assert fib(10) == 55

@pytest.mark.timeout(5)
def test_fib_runtime():
    x = fib(100)
    assert x == 354224848179261915075