def append_and_display_text(file_name, text_to_append):
    with open(file_name, 'a') as file:
        file.write(text_to_append + '\n')

    with open(file_name, 'r') as file:
        content = file.read()

    print("File content after appending:")
    print(content)

file_name = 'example.txt'
text_to_append = "This is the new text to append."

append_and_display_text(file_name, text_to_append)