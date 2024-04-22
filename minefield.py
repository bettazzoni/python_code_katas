class MineField:
    def __init__(self, description_map):
        rows = description_map.split("\n")
        dim_x, dim_y = map(int,  rows[0].split() )
        map_rows = [s.strip() for s in rows[1:] if len(s.strip()) == dim_x]
        self.map = tuple([tuple([1 if c == "*" else 0 for c in row if c in ('.', '*')]) for row in map_rows])
        assert len(self.map) == dim_y

    def bombs(self, x: int, y: int) -> int:
        if x < 0 or y < 0:
            return 0
        try:
            return self.map[y][x]
        except IndexError:
            return 0

    def near_bombs(self, x, y):
        all_possible_neighbourhoods = (
            (x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y),
            (x - 1, y + 1), (x, y + 1), (x + 1, y + 1),)
        return sum([self.bombs(xi, yi) for xi, yi in all_possible_neighbourhoods])

    @property
    def output(self):
        return "\n".join(["".join(['*' if self.map[y][x] else str(self.near_bombs(x, y))
                                   for x in range(len(self.map[0]))])
                          for y in range(len(self.map))])
