class Frame:
    score_values: dict[str, int] = {'X': 10} | {str(i): i for i in range(10)}

    def __init__(self, h1, h2, h3, *the_rest_of_hits):
        def calc_score_of_two_hits(h1, h2):
            return self.score_values[h1] + self.score_values[h2] if h2 != '/' else 10

        if h1 == 'X':   # strike
            self.score = 10 + calc_score_of_two_hits(h2, h3)
            self.hits = 1
        else:
            if h2 == '/':  # spare
                self.score = 10 + self.score_values[h3]
            else:
                self.score = calc_score_of_two_hits(h1, h2)
            self.hits = 2


class Row:
    def __init__(self, row_description):
        s = row_description.replace('-', '0').replace(' ', '0')
        s = s.replace('X0|', 'X|')  # remove the not done try after strikes
        s = s.replace('|', '')
        self.hits_compact_form = s

    def score(self):
        remaining_hits = self.hits_compact_form
        total_score = 0
        while len(remaining_hits) >= 3:
            current_frame = Frame(*remaining_hits)
            total_score += current_frame.score
            remaining_hits = remaining_hits[current_frame.hits:]
        return total_score
