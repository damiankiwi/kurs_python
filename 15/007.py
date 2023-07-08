list1 = [3, 6, 12, 54, 21, 35, 2, 9]
print("Lista 1:", list1)
list2 = [9, 0, 30, 25, 44, 71, 42, 5, 17, 89, 39, 10, 22, 1]
print("Lista 2:", list2)

list3 = input("Wprowadź listę 3, oddzielając je przecinkami: ").split(",")
list3 = [int(x) for x in list3]

max_number_list1 = list1[0]
for number in list1:
    if number > max_number_list1:
        max_number_list1 = number

max_number_list2 = list2[0]
for number in list2:
    if number > max_number_list2:
        max_number_list2 = number

max_number_list3 = list3[0]
for number in list3:
    if number > max_number_list3:
        max_number_list3 = number

print("Największa liczba w liście 1:", max_number_list1)
print("Największa liczba w liście 2:", max_number_list2)
print("Największa liczba w liście 3:", max_number_list3)