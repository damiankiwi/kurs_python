#3. Utwórz dowolną tablicę n x n zawierającą dowolny znak,
# a następnie wyświetl jej elementy w formie tabeli n x n.
# Elementy powinny być oddzielone spacją
"""
wejście:

n = 3

tab = [['-', '-', '-']
  ['-', '-', '-'],
  ['-', '-', '-']]
wyjście:

- - -
- - -
- - -
"""

print('Utwórz dowolną tablicę n x n. Podaj jej wymiary: ')

n = int(input())
tab = [['-'] * n] * n
print(tab)

# for row in tab:
#     for element in row:
#         print(element, end=' ')
#     print()

for row in tab:
    print(' '.join(row))