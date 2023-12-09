def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes_less_than_n(n):
    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    return count

input1 = 10
output1 = count_primes_less_than_n(input1)
print(output1)

input2 = 100
output2 = count_primes_less_than_n(input2)
print(output2)