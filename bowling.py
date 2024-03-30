# Bowling kata "functional programming" version
# thanks to @emadb, translated for the elixir version  https://github.com/emadb/bowling_kata
def score(*hits, frame=1) -> int:
    def following_frames_score(hits_in_this_frame):
        return score(*hits[hits_in_this_frame:], frame=frame + 1)

    def if_spare_add_first_of_next_frame (h1, h2, *next_frame_hits):
        return next_frame_hits[0] if (h1 + h2 == 10) else 0

    if frame <= 10:
        try:
            if hits[0] == 10:
                return hits[0] + hits[1] + hits[2] + following_frames_score(1)
            return hits[0] + hits[1] + if_spare_add_first_of_next_frame(*hits) + following_frames_score(2)
        except IndexError:
            pass
    return 0
