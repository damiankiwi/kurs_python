import itertools
import heapq


def hamming():
    heap = [1]
    seen = {1}
    factors = [2, 3, 5]

    while True:
        hamming_number = heapq.heappop(heap)
        yield hamming_number
        for factor in factors:
            new_hamming_number = hamming_number * factor
            if new_hamming_number not in seen:
                seen.add(new_hamming_number)
                heapq.heappush(heap, new_hamming_number)


def nth_hamming_number(n):
    return next(itertools.islice(hamming(), n - 1, n))


n = 10
print(f"The {n}th Hamming number is: {nth_hamming_number(n)}")

n = 100
print(f"The {n}th Hamming number is: {nth_hamming_number(n)}")