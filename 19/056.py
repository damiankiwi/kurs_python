import math

def find_exponent(a, n):
    x = int(round(math.log(n, a)))
    return x


a1, n1 = 2, 1024
output1 = find_exponent(a1, n1)
print(f"Input:\na = {a1}, n = {n1}\nOutput:\n{output1}")

a2, n2 = 3, 81
output2 = find_exponent(a2, n2)
print(f"\nInput:\na = {a2}, n = {n2}\nOutput:\n{output2}")

a3, n3 = 3, 1290070078170102666248196035845070394933441741644993085810116441344597492642263849
output3 = find_exponent(a3, n3)
print(f"\nInput:\na = {a3}, n = {n3}\nOutput:\n{output3}")