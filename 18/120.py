def totient_function(n):
    result = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            result += 1
    return result

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(totient_function(10))
print(totient_function(15))
print(totient_function(33))