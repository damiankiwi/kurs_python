
def check_variable_type(variable):
    if isinstance(variable, list):
        return "To jest lista."
    elif isinstance(variable, tuple):
        return "To jest tupla."
    elif isinstance(variable, set):
        return "To jest zbiór."
    else:
        return "To nie jest lista, tupla ani zbiór."

my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_set = {7, 8, 9}
my_string = "To jest ciąg znaków"

print(check_variable_type(my_list))
print(check_variable_type(my_tuple))
print(check_variable_type(my_set))
print(check_variable_type(my_string))
