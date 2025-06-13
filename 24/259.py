def test(memory_view):
    for i in range(len(memory_view)):
        memory_view[i] = (memory_view[i] + 10) % 256
def main():
    data = bytearray([100, 200, 150, 200, 50])
    memory_view = memoryview(data)
    print("Original Memory View:", memory_view.tolist())
    test(memory_view)
    print("Modified Memory View:", memory_view.tolist())
if __name__ == "__main__":
    main()