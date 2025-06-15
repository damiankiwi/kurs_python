def main():
    original_data = bytearray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    memory_view = memoryview(original_data)

    start_index = 3
    end_index = 8
    sliced_memory_view = memory_view[start_index:end_index]

    print("Original Data:", original_data)
    print("Sliced Memory View:")
    print(bytearray(sliced_memory_view))
    print(sliced_memory_view.tolist())

if __name__ == "__main__":
    main()