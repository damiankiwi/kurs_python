#7. Usuń duplikat z podanej list i utwórz na jej bazie krotkę.
# Znajdź minimalną i maksymalną liczbę w krotce.


example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

example_set = set(example_list)
print(example_set)

example_tuple = tuple(example_set)
print(example_tuple)

print("MIN:", min(example_tuple))
print("MAX:", max(example_tuple))