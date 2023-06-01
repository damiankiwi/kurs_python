# Write a function called FooBar that takes input integer n and prints all the numbers from 1 upto n in a new line. If the number is divisible by 3 then print "Foo", if the number is divisible by 5 then print "Bar" and if the number is divisible by both 3 and 5, print "FooBar". Otherwise just print the number.
# for example FooBar(15) should print as follows:
# 1
# 2
# Foo
# 4
# Bar
# Foo
# 7
# 8
# Foo
# Bar
# 11
# Foo
# 13
# 14
# FooBar

def foo_bar(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FooBar")
        elif i % 3 == 0:
            print("Foo")
        elif i % 5 == 0:
            print("Bar")
        else:
            print(i)