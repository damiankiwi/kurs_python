#5. Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób,
# natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:

people = [
    ['Dorota', 'Wellman', 'dziennikarka'],
    ['Adam', 'Małysz', 'sportowiec'],
    ['Robert', 'Lewandowski', 'piłkarz'],
    ['Krystyna', 'Janda', 'aktorka']
]
# for row in people:
#     #print(row[0], row[1], '-', row[2])
#     print(" - ".join(row))

print('---------')

for row in people:
    for id, elem in enumerate(row):
        if id == 1:
            print(elem, end=" - ")
        else:
            print(elem, end=" ")
    print()


# print("hello", end=" - ")
# print("kakaka", end="****")
# print("lalala")

# arr = ["ala", "ma", "kota", "i", "psa"]
#
# for value in arr: # pierwszy sposób na fora - po wartościach
#     print(value)
#
#
# for index in range(5): # drugi sposób - po indeksie / numeryczynie
#     if index == 2:
#         print(arr[index], end="***")
#     else:
#         print(arr[index], end="---> ")
#
# print()
# print('*******************')
# for id, word in enumerate(arr):
#     print(id, word)
#     if id == 2:
#         print(word, end="***")
#     else:
#         print(word, end="---> ")
