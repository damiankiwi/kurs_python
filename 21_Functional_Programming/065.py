original_tuple = (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))

def convert_strings_to_int(tuples):
    return tuple(map(lambda t: tuple(int(x) for x in t if x.isdigit()), tuples))

print("Original tuple values:")
print(original_tuple)

converted_tuple = convert_strings_to_int(original_tuple)

print("New tuple values:")
print(converted_tuple)