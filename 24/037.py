# Function to append text to a file and display its content
def append_and_display_text(file_name, text_to_append):
    # Open the file in append mode and write the new text
    with open(file_name, 'a') as file:
        file.write(text_to_append + '\n')

    # Open the file in read mode and display its content
    with open(file_name, 'r') as file:
        content = file.read()

    # Print the content of the file
    print("File content after appending:")
    print(content)

# Specify the file name and the text to append
file_name = 'example.txt'
text_to_append = "This is the new text to append."

# Call the function
append_and_display_text(file_name, text_to_append)