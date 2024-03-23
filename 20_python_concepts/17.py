try:
    while True:
        try:
            number = int(input("Enter a number: "))
            print("You entered:", number)
            break
        except ValueError:
            print("Error: Please enter a valid number.")

except KeyboardInterrupt:
    print("\nInput cancelled by the user.")
