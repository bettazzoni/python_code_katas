NAME_PLAYER_1 = "A"
NAME_PLAYER_2 = "b"

LOVE = "love"
FIFTEEN = "fifteen"
THIRTY = "thirty"
FORTY = "forty"
DEUCE = "deuce"
ADVANTAGE = "advantage"
GAME = "game"
SCORE_STR = ["love", "fifteen", "thirty", "forty", "deuce", "advantage", "game"]


def balls_won(player_won_str):
    return player_won_str.count(NAME_PLAYER_1), player_won_str.count(NAME_PLAYER_2)


def games_score(player_win_sequence):
    a, b = balls_won(player_win_sequence)
    if a < 3 or b < 3:
        return SCORE_STR[a] + "-" + SCORE_STR[b]
    else:
        return DEUCE if a == b else ADVANTAGE + " " + (NAME_PLAYER_1 if a > b else NAME_PLAYER_2)
