def has_odd_product_pair(seq):
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            product = seq[i] * seq[j]
            if product % 2 == 1:
                return True
    return False

sequence = [2, 4, 6, 1, 8, 10]
result = has_odd_product_pair(sequence)
if result:
    print("W sekwencji są dwie liczby, których iloczyn jest liczbą nieparzystą.")
else:
    print("W sekwencji nie ma dwóch liczb, których iloczyn jest liczbą nieparzystą.")
