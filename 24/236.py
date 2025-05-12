def is_descending_sorted(input_list):
    if not input_list:
        return None

    sorted_descending = all(input_list[i] >= input_list[i + 1] for i in range(len(input_list) - 1))
    return sorted_descending

def main():
    try:
        nums = [1, 2, 3, 4, 5]
        result = is_descending_sorted(nums)

        if result is None:
            print("List is empty.")
        elif result:
            print("List is sorted in descending order.")
        else:
            print("List is not sorted in descending order.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()