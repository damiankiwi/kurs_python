def strange_sort(numbers):
    result = []
    numbers.sort()

    while numbers:
        result.append(numbers.pop(0))
        if numbers:
            result.append(numbers.pop(-1))

    return result
input_numbers1 = [1, 3, 4, 5, 11]
output1 = strange_sort(input_numbers1)
print(f"Output 1: {output1}")

input_numbers2 = [27, 3, 8, 5, 1, 31]
output2 = strange_sort(input_numbers2)
print(f"Output 2: {output2}")

input_numbers3 = [1, 2, 7, 3, 4, 5, 6]
output3 = strange_sort(input_numbers3)
print(f"Output 3: {output3}")