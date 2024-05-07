def next_bigger_number(num):
    num_list = list(str(num))

    i = len(num_list) - 1
    while i > 0 and num_list[i - 1] >= num_list[i]:
        i -= 1

    if i == 0:
        return False

    j = len(num_list) - 1
    while num_list[j] <= num_list[i - 1]:
        j -= 1

    num_list[i - 1], num_list[j] = num_list[j], num_list[i - 1]

    num_list[i:] = sorted(num_list[i:])

    return int(''.join(num_list))

numbers = [12, 10, 201, 102, 445]

for number in numbers:
    next_num = next_bigger_number(number)
    print(f"Original number: {number}")
    print(f"Next bigger number: {next_num if next_num else 'False'}")