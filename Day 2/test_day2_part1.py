import pytest

from solution_day2_part1 import run_program

def test_run_program():
    assert run_program([1,0,0,0,99]) == [2,0,0,0,99]
    assert run_program([2,3,0,3,99]) == [2,3,0,6,99]
    assert run_program([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
    assert run_program([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]