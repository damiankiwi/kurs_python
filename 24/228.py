def is_palindrome(string):
    text = ''.join(char.lower() for char in string if char.isalnum())
    return text == text[::-1]

def main():
    try:
        input_string = input("Input a string: ")

        if is_palindrome(input_string):
            print("The string is a palindrome.")
        else:
            print("The string is not a palindrome.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()