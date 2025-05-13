def convert_to_uppercase(input_string):
    if not input_string:
        return None

    return input_string.upper()

def main():
    try:
        str_input = input("Enter a string: ")
        result = convert_to_uppercase(str_input)

        if result is None:
            print("Input is empty.")
        else:
            print("Uppercase result:", result)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()