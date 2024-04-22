import pytest
from minefield_func import read_bomb_map, near_bombs, minefield_output


@pytest.mark.parametrize("field_input,matrix", [
    ('5 3 \n.....\n.....\n.....\n', ( (0,0,0,0,0),
                                      (0,0,0,0,0),
                                      (0,0,0,0,0) )),
    ('6 4 \n*.....\n.*....\n..*...\n.....*\n', ((1, 0, 0, 0, 0, 0),
                                                (0, 1, 0, 0, 0, 0),
                                                (0, 0, 1, 0, 0, 0),
                                                (0, 0, 0, 0, 0, 1))),
 ])
def test_read_bomb_map(field_input, matrix):
    assert read_bomb_map(field_input) == matrix


@pytest.mark.parametrize("input_bomb_map, point, number_of_near_bombs", [
    ( ( (1,0,0,0), (0,1,0,0), (0,0,1,0), (0,0,0,1) ), (1,2), 2),
    ( ( (1,0,0,0), (0,1,0,0), (0,1,0,0), (0,0,0,1) ), (0,1), 3),
    ( ( (1,0,0,0, 0), (0,1,0,0,0), (0,1,0,0,0), (0,0,0,0,1), (0,1,0,0,0) ), (3,3), 1),
    ( ( (1,0,0), (0,1,0), (0,0,1)) , (0,2), 1)
])
def test_near_bombs(input_bomb_map, point, number_of_near_bombs):
    assert near_bombs(input_bomb_map, *point) == number_of_near_bombs

@pytest.mark.parametrize("field_input, output", [
    ( "3 3 \n"
      "*..\n"
      ".*.\n"
      "..*\n", "*21\n2*2\n12*"),
    ( "6 4 \n"
      "*.....\n"
      ".*....\n"
      "..*...\n"
      ".....*\n", "*21000\n2*2100\n12*111\n01111*"),
])
def test_minefield_output(field_input, output):
    assert minefield_output(field_input) == output

