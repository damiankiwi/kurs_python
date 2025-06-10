def concatenate_memory_views(mem_view1, mem_view2):
    result = bytearray(mem_view1) + bytearray(mem_view2)
    return memoryview(result)

def main():
    data1 = bytearray(b"Python ")
    data2 = bytearray(b"Exercises!")
    print("Memory views:")
    memory_view1 = memoryview(data1)
    print(memory_view1)
    memory_view2 = memoryview(data2)
    print(memory_view2)
    concatenated_view = concatenate_memory_views(memory_view1, memory_view2)
    print("Concatenated Memory View:", concatenated_view.tobytes().decode("utf-8"))
if __name__ == "__main__":
    main()