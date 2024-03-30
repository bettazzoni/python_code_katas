# Bowling kata "functional programming" version
# thanks to @emadb, translated for the elixir version  https://github.com/emadb/bowling_kata
def score(*hits, this_frame_number: int = 1) -> int:
    def score_of_following_frames(hits_in_this_frame: int) -> int:
        return score(*hits[hits_in_this_frame:], this_frame_number=this_frame_number + 1)

    def if_spare_add_first_hit_of_next_frame (h1: int, h2: int, *next_frame_hits: tuple) -> int:
        return next_frame_hits[0] if (h1 + h2 == 10) else 0

    if this_frame_number <= 10:
        try:
            if hits[0] == 10:
                return hits[0] + hits[1] + hits[2] + score_of_following_frames(1)
            return hits[0] + hits[1] + if_spare_add_first_hit_of_next_frame(*hits) + score_of_following_frames(2)
        except IndexError:
            pass
    return 0
