numbers = [2, 4, -6, -9, 11, -12, 14, -5, 17]

sum_positive = sum(filter(lambda x: x > 0, numbers))
sum_negative = sum(filter(lambda x: x < 0, numbers))

print("Sum of the positive numbers:", sum_positive)
print("Sum of the negative numbers:", sum_negative)