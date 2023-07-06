sum_even = 0

for number in range(1, 101):
    if number % 2 == 0:
        sum_even += number

print("Suma liczb parzystych: ", sum_even)