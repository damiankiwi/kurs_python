def Is_password_valid(password):
    if len(password) < 8 or len(password) > 16:
        return False

    password_has_digit = any(char.isdigit() for char in password)

    password_special_characters = "!@#$%^&*()_+[]{}|;:,.<>?/"
    has_special_character = any(char in password_special_characters for char in password)

    password_has_uppercase = any(char.isupper() for char in password)
    password_has_lowercase = any(char.islower() for char in password)

    return password_has_digit and has_special_character and password_has_uppercase and password_has_lowercase

def main():
    try:
        password = input("Input your password: ")

        if Is_password_valid(password):
            print("Password is valid.")
        else:
            print("Password is invalid.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()