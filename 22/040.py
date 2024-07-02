import itertools

def chunk_list(iterable, chunk_size):

    iterator = iter(iterable)
    for first in iterator:
        yield list(itertools.islice(itertools.chain([first], iterator), chunk_size))

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = 3

chunks = list(chunk_list(input_list, chunk_size))
print(chunks)