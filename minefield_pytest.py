import pytest
from minefield import Field, MineField


@pytest.mark.parametrize("field_input,matrix", [
    ('5 3 \n.....\n.....\n.....\n', ( (0,0,0,0,0),
                                      (0,0,0,0,0),
                                      (0,0,0,0,0) )),
    ('6 4 \n*.....\n.*....\n..*...\n.....*\n', ((1, 0, 0, 0, 0, 0),
                                                (0, 1, 0, 0, 0, 0),
                                                (0, 0, 1, 0, 0, 0),
                                                (0, 0, 0, 0, 0, 1))),
 ])
def test_set_plateau_dim(field_input, matrix):
    assert Field(field_input).matrix == matrix


@pytest.mark.parametrize("field_input, point, near_bombs", [
    ( "6 4 \n*.....\n.*....\n..*...\n.....*\n", (1,2), 2),
    ( "5 4 \n*....\n.*...\n.*...\n....*\n", (0,1), 3),
    ( "6 4 \n*.....\n.*....\n..*...\n.....*\n", (3,3), 1),
])
def test_near_bombs(field_input, point, near_bombs):
    assert Field(field_input).near_bombs(*point) == near_bombs

@pytest.mark.parametrize("field_input, output", [
    ( "3 3 \n*..\n.*.\n..*\n", "*21\n2*2\n12*"),
    ( "6 4 \n*.....\n.*....\n..*...\n.....*\n", "*21000\n2*2100\n12*111\n01111*"),
])
def test_MineField(field_input, output):
    assert MineField(field_input).output == output

