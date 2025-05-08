def get_middle_character(input_string):
    length = len(input_string)

    if length % 2 == 0:
        return "None"
    else:
        middle_index = length // 2
        return input_string[middle_index]

def main():
    try:
        input_string = input("Input a string: ")
        result = get_middle_character(input_string)

        if result == "None":
            print("String length is even, no middle character.")
        else:
            print("Middle character:", result)
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()