def generate_primes(limit):
    primes = [2]
    num = 3

    while num <= limit:
        for prime in primes:
            if prime * prime > num:
                primes.append(num)
                break
            if num % prime == 0:
                break
        num += 2

    return primes

def find_three_prime_products(limit):
    primes = generate_primes(limit)
    results = []

    for i in range(len(primes)):
        for j in range(i, len(primes)):
            for k in range(j, len(primes)):
                product = primes[i] * primes[j] * primes[k]
                if product <= limit:
                    results.append([primes[i], primes[j], primes[k]])

    return results

limit = 1000
output = find_three_prime_products(limit)
print(f"Input: {limit}")
print(f"Output:")
for result in output:
    print(result)