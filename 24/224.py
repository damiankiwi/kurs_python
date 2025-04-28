def logical_operations(x, y):
    logical_and = x and y
    logical_or = x or y
    return logical_and, logical_or

def main():
    try:
        inputval1 = input("Input first boolean value (True/False): ").lower()
        inputval2 = input("Input second boolean value (True/False): ").lower()

        if inputval1 == "true":
            bool1 = True
        elif inputval1 == "false":
            bool1 = False
        else:
            print("Invalid input for first boolean value.")
            return

        if inputval2 == "true":
            bool2 = True
        elif inputval2 == "false":
            bool2 = False
        else:
            print("Invalid input for second boolean value.")
            return

        logical_and, logical_or = logical_operations(bool1, bool2)
        print(f"Logical AND: {logical_and}")
        print(f"Logical OR: {logical_or}")
    except ValueError:
        print("Invalid input. Please input either 'True' or 'False'.")

if __name__ == "__main__":
    main()