def count_none(input_list):
    if not input_list:
        return 0

    head, *tail = input_list
    if head is None:
        return 1 + count_none(tail)
    else:
        return count_none(tail)

def main():
    try:
        values_list = [None, "Red", None, 8, None, True]
        result = count_none(values_list)

        print("Number of None values:", result)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()