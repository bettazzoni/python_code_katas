import pytest
from game_of_life import Grid, GameOfLife


def test_grid_class():
    N = 4
    M = 10
    g = Grid(N, M, lambda x, y: (x, y))
    for i in range(N):
        for j in range(M):
            assert g.get(i, j) == (i, j), "Grid init error on " + str((i, j))


def test_grid_class_border_wrap():
    N = 11
    M = 7
    g = Grid(N, M, lambda i, j: (i, j))
    for i in range(N * 2):
        for j in range(M * 2):
            assert g.get(i, j) == (i % N, j % M), "Grid wrapping error on " + str((i, j))


def test_grid_class_get_neighbours():
    N = 11
    M = 7
    g = Grid(N, M, lambda i, j: (i, j))
    assert g.get_neighbours(2, 2) == ((1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3))
    assert g.get_neighbours(0, 0) == ((10, 6), (10, 0), (10, 1), (0, 6), (0, 1), (1, 6), (1, 0), (1, 1))


EMPTY_4x8 = (("........",
              "........",
              "........",
              "........")
)

FULL_4x8 = (("********",
             "********",
             "********",
             "********")
)

PASS_1_4x8 = (("........",
               "....*...",
               "...**...",
               "....*...")
)
PASS_2_4x8 = (("........",
               "...**...",
               "...***..",
               "...**...")
)
PASS_3_4x8 = (("........",
               "...*.*..",
               "..*..*..",
               "...*.*..")
)

GLIDER_1 = ((".......",
             "...*...",
             "....*..",
             "..***..",
             "......."))

GLIDER_2 = ((".......",
             ".......",
             "..*.*..",
             "...**..",
             "...*..."))


def test_game_of_life_class_empty():
    gol = GameOfLife.from_strings(EMPTY_4x8)
    for i in range(4):
        for j in range(8):
            assert not gol.get(i, j)


def test_game_of_life_class_full():
    gol = GameOfLife.from_strings(FULL_4x8)
    for i in range(4):
        for j in range(8):
            assert gol.get(i, j)


def test_game_of_life_class_PASS_2_4x8():
    gol = GameOfLife.from_strings(PASS_1_4x8)
    assert gol.matrix[0] == [False] * 8
    assert gol.matrix[1] == [False] * 4 + [True] + [False] * 3
    assert gol.matrix[2] == [False] * 3 + [True, True] + [False] * 3
    assert gol.matrix[3] == [False] * 4 + [True] + [False] * 3


def test_game_of_life_class_grid_by_string():
    assert GameOfLife.from_strings(EMPTY_4x8).get_grid_by_string == EMPTY_4x8
    assert GameOfLife.from_strings(FULL_4x8).get_grid_by_string == FULL_4x8
    assert GameOfLife.from_strings(PASS_1_4x8).get_grid_by_string == PASS_1_4x8
    assert GameOfLife.from_strings(PASS_2_4x8).get_grid_by_string == PASS_2_4x8


@pytest.mark.parametrize("message, grid_str, grid_string_next", (
        ("Test empty grid", EMPTY_4x8, EMPTY_4x8),
        ("Test full grid", FULL_4x8, EMPTY_4x8),
        ("Test PASS1 and PASS2", PASS_1_4x8, PASS_2_4x8),
        ("Test PASS2 and PASS3", PASS_2_4x8, PASS_3_4x8),
        ("Glider", GLIDER_1, GLIDER_2),
))
def test_GameOfLife_generator(message, grid_str, grid_string_next):
    gol_next = GameOfLife.from_strings(grid_str).create_next_generation
    assert gol_next.get_grid_by_string == grid_string_next, message


if __name__ == '__main__':
    pytest.main()
