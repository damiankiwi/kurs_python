def memoryview_to_bytes(mem_view):
    try:
        bytes_data = bytes(mem_view)
        return bytes_data
    except Exception as e:
        print("An error occurred:", e)
        return None


def main():
    try:
        data = b"Python Exercises!"
        mem_view = memoryview(data)
        print("Memory views: ", mem_view)
        bytes_data = memoryview_to_bytes(mem_view)

        if bytes_data is not None:
            print("Bytes Object:", bytes_data)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()