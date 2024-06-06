import itertools


def create_and_display_iterator(*iterables):
    chained_iterator = itertools.chain(*iterables)

    print("Type of the iterator:", type(chained_iterator))

    print("Elements of the iterator:")
    for element in chained_iterator:
        print(element)


list1 = [1, 2, 3]
tuple1 = (4, 5, 6)
set1 = {7, 8, 9}

create_and_display_iterator(list1, tuple1, set1)