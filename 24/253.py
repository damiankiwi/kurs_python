def main():
    try:
        data = b"Python Exercises!"
        mem_data  = memoryview(data)
        print("Memory View Length:", len(mem_data))
        print("First 8 Bytes:", mem_data[:8])
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()