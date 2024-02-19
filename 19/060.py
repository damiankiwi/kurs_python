def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def adjacent_to_prime(numbers):
    result = set()
    for i in range(len(numbers)):
        if i > 0 and is_prime(numbers[i - 1]):
            result.add(numbers[i])
        if i < len(numbers) - 1 and is_prime(numbers[i + 1]):
            result.add(numbers[i])
    return sorted(list(result))

input1 = [2, 17, 16, 0, 6, 4, 5]
output1 = adjacent_to_prime(input1)
print(f"Input:\n{input1}\nOutput:\n{output1}")

input2 = [1, 2, 19, 16, 6, 4, 10]
output2 = adjacent_to_prime(input2)
print(f"\nInput:\n{input2}\nOutput:\n{output2}")

input3 = [1, 2, 3, 5, 1, 16, 7, 11, 4]
output3 = adjacent_to_prime(input3)
print(f"\nInput:\n{input3}\nOutput:\n{output3}")