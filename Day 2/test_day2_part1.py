import pytest

from solution_day2_part1 import intcode_interpreter

def test_intcode_interpreter():
    assert intcode_interpreter([1, 0, 0, 0, 99]) == 2
    assert intcode_interpreter([2, 3, 0, 3, 99]) == 6
    assert intcode_interpreter([2, 4, 4, 5, 99, 0]) == 9801
    assert intcode_interpreter([1, 1, 1, 4, 99, 5, 6, 0, 99]) == 30

def test_input():
    with open("input", "r") as f:
        memory = list(map(int, f.read().strip().split(",")))
    assert intcode_interpreter(memory) == 3101844

