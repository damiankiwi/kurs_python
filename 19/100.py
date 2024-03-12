def find_even_integers(n):
    largest_even = n - (n % 2)

    remaining_sum = n - largest_even

    three_even_integers = [remaining_sum // 3] * 3

    return [largest_even] + three_even_integers


n1 = 100
output1 = find_even_integers(n1)
print(f"Output 1: {output1}")

n2 = 1000
output2 = find_even_integers(n2)
print(f"Output 2: {output2}")

n3 = 10000
output3 = find_even_integers(n3)
print(f"Output 3: {output3}")

n4 = 1234567890
output4 = find_even_integers(n4)
print(f"Output 4: {output4}")