from bowling import Frame, Row
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


if __name__ == '__main__':
    pytest.main()
