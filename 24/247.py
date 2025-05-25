def hex_str_to_bytes(hex_string):
    try:
        bytes_sequence = bytes.fromhex(hex_string)
        return bytes_sequence
    except ValueError as ve:
        print("Error:", ve)
        return None

def main():
    try:
        hex_string = "4861636b657220436f6465"

        bytes_result = hex_str_to_bytes(hex_string)

        if bytes_result is not None:
            print("Hexadecimal String:", hex_string)
            print("Bytes Sequence:", bytes_result)
            print("Decoded String:", bytes_result.decode("utf-8"))
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()