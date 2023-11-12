def sum_of_absolute_differences(arr):
    n = len(arr)
    result = 0

    for i in range(n):
        for j in range(i + 1, n):
            result += abs(arr[i] - arr[j])

    return result

sample_array = [1, 2, 3]
result_sum = sum_of_absolute_differences(sample_array)

print(f"Suma różnic bezwzględnych wszystkich różnych par w tablicy {sample_array}: {result_sum}")