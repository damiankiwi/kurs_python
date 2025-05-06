def check_string(input_string):
    if not input_string:
        return "None"
    return input_string

def main():
    try:
        input_string = input("Input a string: ")
        result = check_string(input_string)
        print("Result:", result)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()