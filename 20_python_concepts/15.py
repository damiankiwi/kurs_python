try:
    file_path = input("Enter the file path: ")

    with open(file_path, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)

except PermissionError:
    print("Error: Permission denied. You don't have the necessary permissions to access the file.")