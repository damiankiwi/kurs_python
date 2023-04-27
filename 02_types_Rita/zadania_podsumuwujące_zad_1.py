#1▹ Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem
# (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
# Następnie powitaj każdą osobę na liście.

name = input('podaj imioną: ')
name_list = name.replace(" ", "").split(',')
for step in name_list:
    print('Hello ', step)

