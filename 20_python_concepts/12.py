try:
    user_input = input("Please enter an integer: ")
    integer_value = int(user_input)
    print("Integer entered:", integer_value)

except ValueError:
    print("Error: Please enter a valid integer.")