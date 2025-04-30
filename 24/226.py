def is_empty_list(lst):
    return not bool(lst)

def main():
    try:
        input_list = eval(input("Input a list (e.g., [1, 2, 3, 4]): "))

        if isinstance(input_list, list):
            if is_empty_list(input_list):
                print("The list is empty.")
            else:
                print("The list is not empty.")
        else:
            print("Invalid input. Please enter a valid list.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()