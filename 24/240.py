def sum_without_none(a, b):
    if a is not None and b is not None:
        return a + b
    else:
        return None

def main():
    try:
        num1 = 3
        num2 = None
        result = sum_without_none(num1, num2)

        if result is None:
            print("At least one argument is None.")
        else:
            print("Sum:", result)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()