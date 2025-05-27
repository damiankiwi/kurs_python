def reverse_bytes(byte_obj):
    reversed_bytes = byte_obj[::-1]
    return reversed_bytes

def main():
    try:
        original_bytes = b"Python Exercises!"

        reversed_result = reverse_bytes(original_bytes)

        print("Original Bytes:", original_bytes)
        print("Reversed Bytes:", reversed_result)
        print("Reversed String:", reversed_result.decode("utf-8"))
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()