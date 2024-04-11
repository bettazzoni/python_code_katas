import operator


class MultipleBookDiscountGroup:
    def __init__(self, singles=0, couple=0, trio=0, quartet=0, all_5books=0):
        self._data = (singles, couple, trio, quartet, all_5books)
        self.one_book_cost = (8.0, 8 * 0.95, 8 * 0.9, 8 * 0.8, 8 * 0.75)

    @property
    def data(self):
        return self._data

    @property
    def cost(self):
        # return sum([ a*b for a,b in zip(self._data, self.one_book_cost)])
        return sum(map(operator.mul, self._data, self.one_book_cost))


def get_index_of_n_different_books(books, return_exact_length):
    index_of_books_present = tuple([i for i in range(len(books)) if books[i] > 0])
    return tuple(index_of_books_present[:return_exact_length]) if len(
        index_of_books_present) >= return_exact_length else ()


def extract_discount_group(books, different_books=2):
    x = list(books)
    eb = get_index_of_n_different_books(x, different_books)
    c = 0
    while eb != ():
        for i in eb:
            x[i] -= 1
        c += different_books
        eb = get_index_of_n_different_books(x, different_books)
    return c, tuple(x)


def split_into_discount_groups(books):
    results ={ (sum(books), 0, 0, 0, 0) }
    discount_group_to_extract = [5, 4, 3, 2]
    while len(discount_group_to_extract)>0:
        x = list(books)
        discount_groups = [0,0,0,0,0]
        for i in discount_group_to_extract:
            discount_groups[i-1], x = extract_discount_group(x, i)
        discount_groups[0] = sum(x)
        results.add(tuple(discount_groups))
        discount_group_to_extract = discount_group_to_extract[1:]
    return results


def hp(hp_books):
    return ()
