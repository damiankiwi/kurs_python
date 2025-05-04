import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def main():
    try:
        email = input("Input an email address: ")

        if is_valid_email(email):
            print("Valid email address!")
        else:
            print("Invalid email address!")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()