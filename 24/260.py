def test(memory_view):
    reversed_memory_view = memory_view[::-1]
    return bytearray(reversed_memory_view)

def main():
    original_data = bytearray([10, 20, 30, 40, 50])
    original_memory_view = memoryview(original_data)
    print("Original Data:", original_data)
    print("Original Memory View:", original_memory_view.tolist())
    reversed_bytearray = test(original_memory_view)
    print("Reversed Bytearray:", reversed_bytearray)
if __name__ == "__main__":
    main()