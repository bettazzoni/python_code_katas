import pytest
from harrypotter import hp, split_into_discount_groups, MultipleBookDiscountGroup, extract_discount_group, \
    get_index_of_n_different_books

@pytest.mark.parametrize("message, number_of_books_for_each_discount, cost", (
        ("zero books", (0, 0, 0, 0, 0), 0),
        ("1 book", (1, 0, 0, 0, 0), 8),
        ("same 2 books", (2, 0, 0, 0, 0), 16),
        ("2 different books", (0, 2, 0, 0, 0), 16.0 - 0.8),
        ("3 different books", (0, 0, 3, 0, 0), 24 * 0.9),
        ("4 different books", (0, 0, 0, 4, 0), 4 * 8 * 0.8),
        ("5 different books", (0, 0, 0, 0, 5), 5 * 8 * 0.75),
        ("5+(3*2) different books", (0, 0, 6, 0, 5), 5 * 8 * 0.75 + 6 * 8 * 0.9),
))
def test_multiple_book_discount_group(message, number_of_books_for_each_discount, cost):
    mbp = MultipleBookDiscountGroup(*number_of_books_for_each_discount)
    assert mbp.data == number_of_books_for_each_discount
    assert mbp.cost == cost
    assert mbp == MultipleBookDiscountGroup(*number_of_books_for_each_discount)


@pytest.mark.parametrize("message, books, return_exact_length, ret", (
        ("zero books and 5 elements return", (0, 0, 0, 0, 0), 5, ()),
        ("1 book and 1 element return", (1, 0, 0, 0, 0), 1, (0,)),
        ("1 book and 2 elements return", (1, 0, 0, 0, 0), 2, ()),
        ("same 3 books and 2 elements return", (3, 0, 0, 0, 0), 2, ()),
        ("2 different books and 2 elements return", (1, 1, 0, 0, 0), 2, (0, 1)),
        ("2 different books and 3 elements return", (1, 1, 0, 0, 0), 3, ()),
        ("3 different books and 2 elements return", (1, 1, 1, 0, 0), 2, (0, 1)),
        ("3 different books and 3 elements return", (4, 1, 1, 0, 0), 3, (0, 1, 2)),
        ("4 different books and 3 elements return", (0, 1, 3, 2, 1), 3, (1, 2, 3)),
        ("4 different books and 4 elements return", (0, 1, 3, 2, 1), 4, (1, 2, 3, 4)),
))
def test_get_index_of_n_different_books(message: str, books: tuple, return_exact_length, ret: tuple):
    assert get_index_of_n_different_books(books, return_exact_length) == ret, message


@pytest.mark.parametrize("message, books, ret", (
        ("zero books", (0, 0, 0, 0, 0), (0, (0, 0, 0, 0, 0))),
        ("1 book", (1, 0, 0, 0, 0), (0, (1, 0, 0, 0, 0))),
        ("same 2 books", (2, 0, 0, 0, 0), (0, (2, 0, 0, 0, 0))),
        ("2 different books", (1, 1, 0, 0, 0), (2, (0, 0, 0, 0, 0))),
        ("3 different books", (1, 1, 1, 0, 0), (2, (0, 0, 1, 0, 0))),
        ("4 different books", (1, 1, 1, 1, 0), (4, (0, 0, 0, 0, 0))),
        ("5 different books", (1, 1, 1, 1, 1), (4, (0, 0, 0, 0, 1))),
        ("odd number", (2, 2, 3, 1, 1), (8, (0, 0, 1, 0, 0))),
))
def test_extract_discount_group_case_2(message: str, books: tuple, ret: tuple):
    assert extract_discount_group(books) == ret, message


@pytest.mark.parametrize("message, books, different_books, ret", (
        ("zero books  ", (0, 0, 0, 0, 0), 3, (0, (0, 0, 0, 0, 0))),
        ("zero books  ", (0, 0, 0, 0, 0), 5, (0, (0, 0, 0, 0, 0))),
        ("1 book      ", (1, 0, 0, 0, 0), 4, (0, (1, 0, 0, 0, 0))),
        ("same 4 books", (4, 0, 0, 0, 0), 3, (0, (4, 0, 0, 0, 0))),
        ("4 different books by 3", (1, 1, 1, 1, 0), 3, (3, (0, 0, 0, 1, 0))),
        ("4 different books by 4", (0, 1, 1, 1, 1), 4, (4, (0, 0, 0, 0, 0))),
        ("5 different books by 4", (2, 2, 3, 1, 2), 4, (8, (0, 0, 1, 0, 1))),
        ("5 different books by 5", (2, 2, 3, 1, 2), 5, (5, (1, 1, 2, 0, 1))),
        ("5 different books by 5 - big nums", (10, 6, 4, 7, 5), 5, (20, (6, 2, 0, 3, 1))),
))
def test_extract_discount_group_other_cases(message: str, books: tuple, different_books, ret: tuple):
    assert extract_discount_group(books, different_books) == ret, message


@pytest.mark.parametrize("message, books, number_of_books_for_each_discount", (
        ("zero books", (0, 0, 0, 0, 0), {(0, 0, 0, 0, 0), }),
        ("1 book", (1, 0, 0, 0, 0), {(1, 0, 0, 0, 0), }),
        ("same 2 books", (2, 0, 0, 0, 0), {(2, 0, 0, 0, 0), }),
        ("2 different books", (1, 1, 0, 0, 0), {(2, 0, 0, 0, 0), (0, 2, 0, 0, 0)}),
        ("3 different books #1", (0, 1, 1, 1, 0), {(3, 0, 0, 0, 0), (1, 2, 0, 0, 0), (0, 0, 3, 0, 0)}),
        ("3 different books #2", (1, 0, 0, 1, 1), {(3, 0, 0, 0, 0), (1, 2, 0, 0, 0), (0, 0, 3, 0, 0)}),
        ("4 different books   ", (1, 1, 0, 1, 1), {(4, 0, 0, 0, 0), (0, 4, 0, 0, 0), (1, 0, 3, 0, 0), (0, 0, 0, 4, 0)}),
        ("5 different books   ", (1, 1, 1, 1, 1),
         {(5, 0, 0, 0, 0), (1, 4, 0, 0, 0), (0, 2, 3, 0, 0), (1, 0, 0, 4, 0), (0, 0, 0, 0, 5)}),
        ("5*2 different books ", (2, 2, 2, 2, 2),
         {(10, 0, 0, 0, 0), (2, 8, 0, 0, 0), (0, 4, 6, 0, 0), (2, 0, 0, 8, 0), (0, 0, 0, 0, 10)}),
        ("example in spec", (2, 2, 2, 1, 1),
         {(8, 0, 0, 0, 0), (0, 8, 0, 0, 0), (0, 2, 6, 0, 0), (0, 0, 0, 8, 0), (0, 0, 3, 0, 5)}),
))
def test_split_into_discount_groups(message: str, books: tuple, number_of_books_for_each_discount: tuple):
    assert split_into_discount_groups(books) == number_of_books_for_each_discount, message


@pytest.mark.parametrize("message, books, result", (
        ("zero books", (0, 0, 0, 0, 0),
         { MultipleBookDiscountGroup(0, 0, 0, 0, 0)}),
        ("2 identical books", (2, 0, 0, 0, 0),
         { MultipleBookDiscountGroup(2, 0, 0, 0, 0)}),
        ("2 different", (0, 1, 1, 0, 0),
         { MultipleBookDiscountGroup(0, 2, 0, 0, 0),
           MultipleBookDiscountGroup(2, 0, 0, 0, 0),
           }),
        ("example", (2, 2, 2, 1, 1),
         {MultipleBookDiscountGroup(8, 0, 0, 0, 0),
          MultipleBookDiscountGroup(0, 8, 0, 0, 0),
          MultipleBookDiscountGroup(0, 2, 6, 0, 0),
          MultipleBookDiscountGroup(0, 0, 0, 8, 0),
          MultipleBookDiscountGroup(0, 0, 3, 0, 5),
          }),
))
def test_hp(message: str, books: tuple, result: tuple):
    assert hp(books) == result, message


if __name__ == '__main__':
    pytest.main()
