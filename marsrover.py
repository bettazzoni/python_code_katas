HEADINGS = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
TURN_RIGHT = {'N': (1, 0), 'E': (0, -1), 'S': (-1, 0), 'W': (0, 1)}
TURN_LEFT = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}


class Rover:
    plateau_dim = (0, 0)

    @classmethod
    def set_plateau_dim(cls, plateau_dimension_line):
        numbers = [int(x) for x in plateau_dimension_line.split() if x.isnumeric()]
        cls.plateau_dim = tuple(numbers)

    def __init__(self, start_position_str):
        s = start_position_str.split()
        self.pos = (int(s[0]), int(s[1]))
        self.heading = HEADINGS[s[2]]

    @property
    def heading_letter(self):
        return {i for i in HEADINGS if HEADINGS[i] == self.heading}.pop()

    @property
    def position(self):
        return "%d %d %s" % (self.pos[0], self.pos[1], self.heading_letter)

    def move(self, move_str):
        actions = {'M': lambda: ((self.pos[0] + self.heading[0], self.pos[1] + self.heading[1]), self.heading),
                   'R': lambda: (self.pos, TURN_RIGHT[self.heading_letter]),
                   'L': lambda: (self.pos, TURN_LEFT[self.heading_letter])
                   }
        for ch in move_str.strip():
            self.pos, self.heading = actions[ch]()
        return self.position


def kata_solution(input_str):
    text_rows = [r.strip() for r in input_str.split('\n') if len(r.strip()) > 0]
    Rover.set_plateau_dim(text_rows[0])
    return "\n".join([Rover(text_rows[i]).move(text_rows[i + 1]) for i in range(1, len(text_rows), 2)])
