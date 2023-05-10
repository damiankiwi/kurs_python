#2. Utwórz listę lub krotkę tuples_to_dict zawierającą krotki 2 elementowe.
# Przekształć ją w słownik dict_from_tuples.

tuples_to_dict = [("kot", "cat"), ("pies", "dog")]

dict_from_tuples = dict(tuples_to_dict)
print(dict_from_tuples)

for k, v in dict_from_tuples.items():
    print(k, '-->', v)