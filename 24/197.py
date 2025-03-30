import heapq

def nth_Super_Ugly_Number(n, primes):
    uglies = [1]

    def gen(prime):
        for ugly in uglies:
            yield ugly * prime

    merged = heapq.merge(*map(gen, primes))
    while len(uglies) < n:
        ugly = next(merged)
        if ugly != uglies[-1]:
            uglies.append(ugly)
    return uglies[-1]
n = 12
primes = [2,7,13,19]
print(nth_Super_Ugly_Number(n, primes))