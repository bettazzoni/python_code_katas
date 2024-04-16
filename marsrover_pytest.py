import pytest
from marsrover import Rover, kata_solution, NORD, EAST, SOUTH, WEST, Position


@pytest.mark.parametrize("plateau_dimension_line,plateau_dim_tuple", [
    ('1 6', (1, 6)),
    ('5 5\n', (5, 5)),
    ('745\t101  ', (745, 101)),
])
def test_set_plateau_dim(plateau_dimension_line, plateau_dim_tuple):
    Rover.set_plateau_dim(plateau_dimension_line)
    assert Rover.plateau_dim == plateau_dim_tuple
    assert Rover("0 0 S").plateau_dim == plateau_dim_tuple


@pytest.mark.parametrize("rover_start_str, rover_pos", [
    ('10 20 N  \n ', Position(10, 20, NORD) ),
    ('0 0 E       ', Position(0, 0, EAST) ),
    ('137\t42 W\n ', Position(137, 42, WEST) ),
])
def test_constructor(rover_start_str, rover_pos):
    r = Rover(rover_start_str)
    assert r.pos == rover_pos


def test_position():
    r = Rover(" 101  69  S")
    assert r.position == "101 69 S"


@pytest.mark.parametrize("start_str, move_str, result_position", [
    ('0 0 E ', "M", "1 0 E"),
    ('1 1 N ', "RM", "2 1 E"),
    ('1 2 N ', "LMLMLMLMM", "1 3 N"),
    ('3 3 E ', "MMRMMRMRRM", "5 1 E"),
])
def test_move(start_str, move_str, result_position):
    r = Rover(start_str)
    assert r.move(move_str) == result_position


def test_kata_solution():
    inp = ("5 5\n"
           "\n"
           "1 2 N\n"
           "LMLMLMLMM\n"
           "\n"
           "3 3 E\n"
           "MMRMMRMRRM\n")
    assert kata_solution(inp) == "1 3 N\n5 1 E"
