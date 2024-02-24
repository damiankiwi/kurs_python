def find_fives(n):
    result = []

    for i in range(5, n):
        if i % 9 == 0 or i % 15 == 0:
            count_of_fives = str(i).count('5')
            result.append([i, count_of_fives])

    return result

n_values = [50, 65, 75, 85, 150]

for n in n_values:
    output = find_fives(n)
    print(f"Value of n = {n}")
    print("Output:")
    print(output)
    print()