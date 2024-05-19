def average_of_tuples(tuples):
    transposed = zip(*tuples)
    averages = tuple(map(lambda x: sum(x) / len(x), transposed))
    return averages

tuple1 = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
print("Original Tuple:")
print(tuple1)
print("Average value of the numbers of the said tuple of tuples:")
print(average_of_tuples(tuple1))

tuple2 = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
print("\nOriginal Tuple:")
print(tuple2)
print("Average value of the numbers of the said tuple of tuples:")
print(average_of_tuples(tuple2))