import sys
import os
import pytest
import random
import math

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from factorial import factorial

def test_factorial_0():
    assert factorial(0) == 1

def test_factorial_1():
    assert factorial(1) == 1

def test_factorial_10_random():
    for _ in range(10):
        n = random.randint(2, 10)
        assert factorial(n) == math.factorial(n)