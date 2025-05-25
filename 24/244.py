def concatenate_bytes(byte_obj1, byte_obj2):
    concatenated_bytes = byte_obj1 + byte_obj2
    return concatenated_bytes

def main():
    try:
        str_bytes1 = b"Python "
        str_bytes2 = b"Exercises!"
        concatenated_result = concatenate_bytes(str_bytes1, str_bytes2)
        print("Bytes 1:", str_bytes1)
        print("Bytes 2:", str_bytes2)
        print("Concatenated Bytes:", concatenated_result)
        print("Concatenated String:", concatenated_result.decode("utf-8"))
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
