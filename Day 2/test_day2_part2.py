import pytest

from solution_day2_part2 import find_inputs
from solution_day2_part2 import run_intcode


def test_run_intcode():
    mem = [1,0,0,0,99]
    assert run_intcode(mem) == [2,0,0,0,99]

    mem = [2,3,0,3,99]
    assert run_intcode(mem) == [2,3,0,6,99]

    mem = [2,4,4,5,99,0]
    assert run_intcode(mem) == [2,4,4,5,99,9801]

    mem = [1,1,1,4,99,5,6,0,99]
    assert run_intcode(mem) == [30,1,1,4,2,5,6,0,99]

def test_find_inputs():
    memory = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,2,9,23,27,1,6,27,31,1,31,9,35,2,35,10,39,1,5,39,43,2,43,9,47,1,5,47,51,1,51,5,55,1,55,9,59,2,59,13,63,1,63,9,67,1,9,67,71,2,71,10,75,1,75,6,79,2,10,79,83,1,5,83,87,2,87,10,91,1,91,5,95,1,6,95,99,2,99,13,103,1,103,6,107,1,107,5,111,2,6,111,115,1,115,13,119,1,119,2,123,1,5,123,0,99,2,0,14,0]
    noun, verb = find_inputs(memory, 19690720)
    assert 100 * 12 + 2 == 1202


