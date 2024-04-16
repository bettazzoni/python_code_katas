from collections import namedtuple

CardinalDirection = namedtuple('CardinalDirection', ['letter', 'x', 'y', 'turn_right', 'turn_left'])

NORD = CardinalDirection('N', 0, 1, 'E', 'W')
EAST = CardinalDirection('E', 1, 0, 'S', 'N')
SOUTH = CardinalDirection('S', 0, -1, 'W', 'E')
WEST = CardinalDirection('W', -1, 0, 'N', 'S')

CARDINAL_POINTS = {h.letter: h for h in (NORD, EAST, SOUTH, WEST)}

Position = namedtuple('Position', ['x', 'y', "direction"])


class Rover:
    plateau_dim = (0, 0)

    @classmethod
    def set_plateau_dim(cls, plateau_dimension_line: str):
        numbers = [int(x) for x in plateau_dimension_line.split() if x.isnumeric()]
        cls.plateau_dim = tuple(numbers)

    def __init__(self, start_position_str):
        s = start_position_str.split()
        self.pos = Position(int(s[0]), int(s[1]), CARDINAL_POINTS[s[2]])

    @property
    def position(self):
        return "%d %d %s" % (self.pos.x, self.pos.y, self.pos.direction.letter)

    def move(self, move_str: str):
        actions = dict(M=lambda: Position(self.pos.x + self.pos.direction.x,
                                          self.pos.y + self.pos.direction.y,
                                          self.pos.direction),
                       R=lambda: self.pos._replace(direction=CARDINAL_POINTS[self.pos.direction.turn_right]),
                       L=lambda: self.pos._replace(direction=CARDINAL_POINTS[self.pos.direction.turn_left]))
        for ch in move_str.strip():
            self.pos = actions[ch]()
        return self.position


def kata_solution(input_str: str):
    text_rows = [r.strip() for r in input_str.split('\n') if len(r.strip()) > 0]
    Rover.set_plateau_dim(text_rows[0])
    return "\n".join([Rover(text_rows[i]).move(text_rows[i + 1]) for i in range(1, len(text_rows), 2)])
