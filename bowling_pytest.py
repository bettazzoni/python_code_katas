from bowling import Frame, Row
import bowling_func
import pytest


@pytest.mark.parametrize("hits_compact, frame_score, hits_in_frame", (
        ("00*", 0, 2),
        ("11?", 2, 2),
        ("25?", 7, 2),
        ("1/0", 10, 2),
        ("1/1", 11, 2),
        ("5/X", 20, 2),
        ("X53", 18, 1),
        ("X5/", 20, 1),
        ("X00", 10, 1),
        ("XXX", 30, 1),
))
def test_frame_class_valid_hits(hits_compact, frame_score, hits_in_frame):
    fr = Frame(*hits_compact)
    assert fr.score == frame_score, "Score error "
    assert fr.hits == hits_in_frame, "Hits error "


def test_row_compact():
    assert Row("  |  |  |  |  |  |  |  |  |  ||  ").hits_compact_form == "0000000000000000000000"
    assert Row("12|34|5-|-8|90|12|34|-6|-8|90||X0").hits_compact_form == "12345008901234060890X0"
    assert Row("12|X |0/|--|X-|12|34|- |71|9 ||3/").hits_compact_form == "12X0/00X12340071903/"
    assert Row("X |7/|9-|X |-8|8/|-6|X |X |X ||X ").hits_compact_form == "X7/90X088/06XXXX0"


@pytest.mark.parametrize("row, score_of_the_row", (
        ("  |  |  |  |  |  |  |  |  |  ||  ", 0),
        ("1 |  |  |  |  |  |  |  |  |  ||  ", 1),
        ("12|  |  |  |  |  |  |  |  |  ||  ", 3),
        ("1 |1 |1 |1 |1 |1 |1 |1 |1 |1 ||  ", 10),
        ("9 |9 |9 |9 |9 |9 |9 |9 |9 |9 ||  ", 90),
        ("1/|  |  |  |  |  |  |  |  |  ||  ", 10),
        ("1/|1/|  |  |  |  |  |  |  |  ||  ", 21),
        ("1/|8 |  |  |  |  |  |  |  |  ||  ", 26),
        ("1/|8 |  |  |  |  |  |  |  |  ||  ", 26),
        (" /| /| /| /| /| /| /| /| /| /||  ", 100),
        ("5/|5/|5/|5/|5/|5/|5/|5/|5/|5/||5 ", 150),
        ("X |  |  |  |  |  |  |  |  |  ||  ", 10),
        ("X |23|  |  |  |  |  |  |  |  ||  ", 20),
        ("X |2/|  |  |  |  |  |  |  |  ||  ", 30),
        ("X |2/|X |  |  |  |  |  |  |  ||  ", 50),
        ("--|  |  |  |  |  |  |  |  |X ||11", 12),
        ("  |2/|X |  |  |  |  |  |  |X ||--", 40),
        ("  |2/|X |  |  |  |  |  |  |X ||X ", 50),
        ("  |2/|X |  |  |  |  |  |  |X ||XX", 60),
        ("  |--|--|  |  |  |  |  |X |34||  ", 24),
        ("X |X |X |X |X |X |X |X |X |X ||XX", 300),
        ("X |7/|9-|X |-8|8/|-6|X |X |X ||8/", 168),
        ("X |7/|9-|X |-8|8/|-6|X |X |X ||X-", 170),
        ("X |7/|9-|X |-8|8/|-6|X |X |X ||81", 167),
))
def test_row(row, score_of_the_row):
    assert Row(row).score() == score_of_the_row



@pytest.mark.parametrize("message, expected, hits_sequence", (
        ("empty", 0, ()),
        ("All zeros", 0, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)),
        ("All ones", 20, (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)),
        ("One Strike", 24, (10, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)),
        ("One Spare", 16, (5, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)),
        ("Quasi All Spare", 75, (5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)),
        ("All Spare all 5s", 150, (5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)),
        ("All Spare 0 & 10s", 100, (0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0)),
        ("Quasi perfect game", 270, (10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)),
        ("Perfect game", 300, (10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)),
        ("nines", 90, (9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0)),
        ("Other cases #1", 81, (6, 2, 6, 2, 2, 5, 5, 5, 0, 9, 9, 0, 6, 4, 10, 0, 0, 0, 0)),
        ("Other cases #2", 113, (6, 2, 6, 2, 2, 5, 5, 5, 0, 9, 9, 0, 6, 4, 10, 5, 2, 9, 1, 8)),
        ("Other cases #3", 89, (8, 0, 3, 0, 9, 0, 1, 3, 5, 2, 1, 4, 1, 6, 10, 2, 8, 5, 5, 1)),
        ("Other cases #4", 90, (9, 0, 4, 3, 5, 4, 6, 4, 5, 4, 4, 4, 8, 0, 7, 3, 1, 7, 4, 2)),
        ("Other cases #5", 85, (8, 2, 5, 0, 2, 6, 0, 7, 6, 3, 0, 10, 2, 5, 3, 0, 3, 2, 8, 2, 4)),
        ("Uncle Bob last", 167, (10, 7, 3, 9, 0, 10, 0, 8, 8, 2, 0, 6, 10, 10, 10, 8, 1)),
        ("9th frame Strike", 24, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 3, 4)),
))
def test_hits_sequence(message, expected, hits_sequence):
    assert bowling_func.score(*hits_sequence) == expected, message


if __name__ == '__main__':
    pytest.main()
