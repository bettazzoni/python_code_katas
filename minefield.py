from collections import namedtuple

Position = namedtuple('Position', ['x', 'y'])


class Field:
    def __init__(self, description_map):
        rows = description_map.split("\n")
        s = rows[0].split()
        self.dim = Position(int(s[0]), int(s[1]))
        map_rows = [s.strip() for s in rows[1:] if len(s.strip()) == self.dim.x]
        self.matrix = tuple([tuple([1 if c == "*" else 0 for c in row if c in ('.', '*')]) for row in map_rows])
        assert len(self.matrix) == self.dim.y

    def near_bombs(self, x, y):
        all_possible_neighbourhood = (
            (x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y),
            (x - 1, y + 1), (x, y + 1), (x + 1, y + 1),)
        a = [self.matrix[yi][xi]
             for xi, yi in all_possible_neighbourhood
             if 0 <= xi < self.dim.x and 0 <= yi < self.dim.y]
        return sum(a)


class MineField(Field):
    def __init__(self, description_map):
        super().__init__(description_map)

    @property
    def output(self):
        return "\n".join(["".join(['*' if self.matrix[y][x] else str(self.near_bombs(x, y))
                                   for x in range(self.dim.x)])
                          for y in range(self.dim.y)])
