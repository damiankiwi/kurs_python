try:
    file_path = input("Enter the file path: ")
    with open(file_path, 'r') as file:
        print("File contents:")
        print(file.read())

except FileNotFoundError:
    print("Error: File not found. Please make sure the file path is correct.")