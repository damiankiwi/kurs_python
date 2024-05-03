names = ['Adam', 'john', 'Lucy', 'peter', 'Emily', 'Tom']

total_length = sum(map(lambda x: len(x), filter(lambda x: x[0].isupper(), names)))

print("Result:")
print(total_length)