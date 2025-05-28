def are_bytes_equal(bytes_obj1, bytes_obj2):
    return bytes_obj1 == bytes_obj2

def main():
    try:
        bytes_obj1 = b"Python"
        bytes_obj2 = b"Java"
        bytes_obj3 = b"Exercises"
        bytes_obj4 = b"Python"

        are_equal_obj1_obj2 = are_bytes_equal(bytes_obj1, bytes_obj2)
        are_equal_obj1_obj3 = are_bytes_equal(bytes_obj1, bytes_obj3)
        are_equal_obj1_obj4 = are_bytes_equal(bytes_obj1, bytes_obj4)

        print("Bytes Object-1:", bytes_obj1)
        print("Bytes Object-2:", bytes_obj2)
        print("Bytes Object-3:", bytes_obj3)

        print("\nAre Bytes Object-1 and Object-2 equal?", are_equal_obj1_obj2)
        print("Are Bytes Object-1 and Object-3 equal?", are_equal_obj1_obj3)
        print("Are Bytes Object-1 and Object-4 equal?", are_equal_obj1_obj4)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()