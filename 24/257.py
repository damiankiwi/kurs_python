def modify_file_data(data):
    for i in range(len(data)):
        data[i] = (data[i] + 10) % 256

def main():
    input_file_path = "fontawesome_webfont.bin"
    output_file_path = "output.bin"

    with open(input_file_path, "rb") as input_file:
        input_data = input_file.read()
        input_bytearray = bytearray(input_data)

    memory_view = memoryview(input_bytearray)

    modify_file_data(memory_view)

    with open(output_file_path, "wb") as output_file:
        output_file.write(memory_view)

    print("File modification complete.")

if __name__ == "__main__":
    main()