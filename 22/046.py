def extract_uppercase_letters(input_list):
    combined_string = ''.join(input_list)

    uppercase_letters = list(filter(lambda x: x.isupper(), combined_string))

    return uppercase_letters

input_list = ['Hello', 'World', 'PYTHON', 'programming', 'Is', 'Fun']
uppercase_letters = extract_uppercase_letters(input_list)
print(f"Uppercase letters: {uppercase_letters}")