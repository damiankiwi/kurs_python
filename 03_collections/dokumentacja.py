#https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

"""hobbits = ["oko", "nos", "ucho"]
           # 0      1       2
#Element o indeksie 1:

hobbits[1]
print(hobbits[1])"""

#1. Metoda która utworzy kopię listy

list = [1, 2, 3]
list2 = list.copy()

print(list2)

"""Zad 1 
>>> arr = [3, 5, 6, 7, 9, 2 ]
>>> copy_arr = arr[ : ]
>>> print(copy_arr)
[3, 5, 6, 7, 9, 2]
>>> print(copy_arr)
[3, 5, 6, 7, 9, 2]
>>> copy_arr2 = arr.copy()
>>> copy_arr2
[3, 5, 6, 7, 9, 2]"""

#2. Metoda która posrotuje elementy na liście

list = [4, 6, 1, 5, 3, 7]

list.sort()
print(list.sort())

""">>> arr
[3, 5, 6, 7, 9, 2]
>>> arr.sort()
>>> arr
[2, 3, 5, 6, 7, 9]
>>> arr2 = [4, 6, 1, 5, 3, 7]
>>> sorted(arr2)
[1, 3, 4, 5, 6, 7]
>>> print(arr2)
[4, 6, 1, 5, 3, 7]
>>> arr2_sorted = sorted(arr2)
>>> print(arr2_sorted)
[1, 3, 4, 5, 6, 7]
>>> print(arr2)
[4, 6, 1, 5, 3, 7]"""


#3. Jaka metoda usunie wsztystkie lementy z listy?

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]



#4. Policzy wystapienia takiego samego elemtnu na liscie

""">>> arr = [ 3, 5, 7, 2, 4, 2, 6, 2]
>>> arr.count(2)

sum(arr)

"""

