def is_perfect_number(num):

    if num <= 0:
        return False

    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i

    return divisor_sum == num

print(is_perfect_number(6))    #True
print(is_perfect_number(28))   #True
print(is_perfect_number(496))  #True
print(is_perfect_number(8128)) #True
print(is_perfect_number(10))   #False