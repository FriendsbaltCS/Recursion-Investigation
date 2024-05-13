import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hanoi import solve

def test_hanoi_0(capfd):
    solve(0)
    captured = capfd.readouterr()
    assert captured.out == ""

def test_hanoi_1(capfd):
    solve(1)
    captured = capfd.readouterr()
    test_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hanoi_solutions', 'hanoi_1.txt')
    with open(test_file_path, 'r', encoding='utf-16') as f:
        correct_solution = f.read()
    assert captured.out == correct_solution

def test_hanoi_3(capfd):
    solve(3)
    captured = capfd.readouterr()

    test_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hanoi_solutions', 'hanoi_3.txt')
    with open(test_file_path, 'r', encoding='utf-16') as f:
        correct_solution = f.read()
    assert captured.out == correct_solution

def test_hanoi_5(capfd):
    solve(5)
    captured = capfd.readouterr()
    test_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hanoi_solutions', 'hanoi_5.txt')
    with open(test_file_path, 'r', encoding='utf-16') as f:
        correct_solution = f.read()
    assert captured.out == correct_solution

def test_hanoi_9(capfd):
    solve(9)
    captured = capfd.readouterr()
    test_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hanoi_solutions', 'hanoi_9.txt')
    with open(test_file_path, 'r', encoding='utf-16') as f:
        correct_solution = f.read()
    assert captured.out == correct_solution