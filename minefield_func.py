def read_bomb_map(description_map):
    rows = description_map.split("\n")
    dim_x, dim_y = map(int, rows[0].split())
    map_rows = [s.strip() for s in rows[1:] if len(s.strip()) == dim_x]
    bomb_map = tuple([tuple([1 if c == "*" else 0 for c in row if c in ('.', '*')]) for row in map_rows])
    assert len(bomb_map) == dim_y
    return bomb_map


def near_bombs(bomb_map, x, y):
    def safe_get_bomb(xb: int, yb: int) -> int:
        try:
            return 0 if xb < 0 or yb < 0 else bomb_map[yb][xb]
        except IndexError:
            return 0

    neighbourhoods = ((x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1))
    return sum([safe_get_bomb(xi, yi) for xi, yi in neighbourhoods])


def minefield_output(description_map):
    bomb_map = read_bomb_map(description_map)
    x_dim, y_dim = len(bomb_map[0]), len(bomb_map)
    return "\n".join(["".join(['*' if bomb_map[y][x] else str(near_bombs(bomb_map, x, y)) for x in range(x_dim)])
                      for y in range(y_dim)])
