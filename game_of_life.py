class Grid():
    def __init__(self, N, M, init_function):
        self.N = N
        self.M = M
        self.matrix = [[init_function(i, j) for j in range(M)] for i in range(N)]

    def get(self, i, j):
        return self.matrix[i % self.N][j % self.M]

    def get_neighbours(self, i, j):
        return (self.get(i - 1, j - 1), self.get(i - 1, j), self.get(i - 1, j + 1), self.get(i, j - 1),
                self.get(i, j + 1), self.get(i + 1, j - 1), self.get(i + 1, j), self.get(i + 1, j + 1))


class GameOfLife(Grid):
    def __init__(self, N, M, init_function):
        super().__init__(N, M, init_function)

    @property
    def get_grid_by_string(self):
        return tuple([''.join(['*' if el else '.' for el in row]) for row in self.matrix])

    @classmethod
    def from_strings(cls, strings):
        return cls(N=len(strings), M=len(strings[0]), init_function=lambda x, y: (strings[x][y] == '*'))

    @classmethod
    def from_matrix(cls, matrix, set_func):
        return cls(N=len(matrix), M=len(matrix[0]), init_function=set_func)

    @property
    def create_next_generation(self):
        def set_func(i, j):
            living_neighbours: int = sum([1 for _ in self.get_neighbours(i, j) if _])
            return living_neighbours == 3 or (self.get(i, j) and living_neighbours == 2)
        return self.from_matrix(self.matrix, set_func)


# as demo print the glider sequence
if __name__ == '__main__':
    GLIDER = ((".............",
               ".............",
               "......*......",
               ".......*.....",
               ".....***.....",
               ".............",
               "............."))


    def print_tabbed(g):
        for i in gof.get_grid_by_string:
            print(i)
        print()


    gof = GameOfLife.from_strings(GLIDER)
    print_tabbed(gof)
    for i in range(4):
        gof = gof.create_next_generation
        print_tabbed(gof)
