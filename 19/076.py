def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def largest_prime_index_and_sum(lst):
    max_prime_index = -1
    max_prime_sum = -1

    for i, num in enumerate(lst):
        if is_prime(num):
            current_sum = sum_of_digits(num)
            if current_sum > max_prime_sum:
                max_prime_sum = current_sum
                max_prime_index = i

    return [max_prime_index, max_prime_sum]

input1 = [3, 7, 4]
output1 = largest_prime_index_and_sum(input1)

input2 = [3, 11, 7, 17, 19, 4]
output2 = largest_prime_index_and_sum(input2)

input3 = [23, 17, 201, 14, 10473, 43225, 421, 423, 11, 10, 2022, 342157]
output3 = largest_prime_index_and_sum(input3)

print(f"Input 1: {input1}")
print(f"Output 1: {output1}")

print(f"Input 2: {input2}")
print(f"Output 2: {output2}")

print(f"Input 3: {input3}")
print(f"Output 3: {output3}")