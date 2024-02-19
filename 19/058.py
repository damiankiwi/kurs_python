def find_largest_even(m, n):
    largest_even = 0

    for num in range(n, m - 1, -1):
        if num % 2 == 0:
            largest_even = num
            break

    return largest_even

m1, n1 = 12, 51
output1 = find_largest_even(m1, n1)
print(f"Input:\nm = {m1}\nn = {n1}\nOutput:\n{output1}")

m2, n2 = 1, 79
output2 = find_largest_even(m2, n2)
print(f"\nInput:\nm = {m2}\nn = {n2}\nOutput:\n{output2}")

m3, n3 = 47, 53
output3 = find_largest_even(m3, n3)
print(f"\nInput:\nm = {m3}\nn = {n3}\nOutput:\n{output3}")

m4, n4 = 100, 200
output4 = find_largest_even(m4, n4)
print(f"\nInput:\nm = {m4}\nn = {n4}\nOutput:\n{output4}")