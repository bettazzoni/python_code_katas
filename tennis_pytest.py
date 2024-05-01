import pytest
from tennis import balls_won, games_score, LOVE, FIFTEEN, THIRTY, FORTY, DEUCE, ADVANTAGE


@pytest.mark.parametrize("player_win_sequence, balls_won_tuple", (
        ("A", (1,0)),
        ("b", (0,1)),
        ("Abbb", (1,3)),
        ("bbAAbAA", (4,3)),
        ("AbAAbbAAb", (5,4)),
))
def test_balls_won( player_win_sequence, balls_won_tuple):
    assert balls_won(player_win_sequence) == balls_won_tuple


@pytest.mark.parametrize("player_win_sequence, score", (
        ("A", FIFTEEN + "-" + LOVE),
        ("b", LOVE + "-" + FIFTEEN),
        ("Abbb", FIFTEEN + "-" + FORTY),
        ("bAAbA", FORTY+"-"+THIRTY),
        ("bAAbAb", DEUCE),
        ("bAAbAbA", ADVANTAGE + " A"),
        ("bAAbAbAbbAAbb", ADVANTAGE + " b"),
))
def test_game_score( player_win_sequence, score):
    assert games_score(player_win_sequence) == score


if __name__ == '__main__':
    pytest.main()
