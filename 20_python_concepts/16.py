try:
    my_list = [1, 2, 3, 4, 5]

    index = int(input("Enter the index to access: "))
    value = my_list[index]
    print("Value at index", index, "is:", value)

except IndexError:
    print("Error: Index out of range. Please provide a valid index within the range of the list.")