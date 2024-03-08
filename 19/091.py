def generate_numbers(n):
    numbers = []

    for i in range(10**(n-1), 10**n):
        str_i = str(i)

        if str_i.startswith('2') or str_i.endswith('2'):
            numbers.append(i)

    return numbers

input_n = int(input("Enter the value of n: "))
output = generate_numbers(input_n)
print(f"Output: {output}")