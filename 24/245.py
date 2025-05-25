def bytearray_from_list(int_list):
    byte_array = bytearray(int_list)
    return byte_array

def main():
    try:
        nums = [72, 123, 21, 108, 222, 67, 44, 38, 10]

        byte_array_result = bytearray_from_list(nums)

        print("Integer List:", nums)
        print("Bytearray:", byte_array_result)
        print("Decoded String:", byte_array_result.decode("utf-8"))
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
