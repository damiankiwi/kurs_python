def insert_none(input_list):
    new_list = []
    for item in input_list:
        new_list.append(item)
        new_list.append(None)
    new_list.pop()
    return new_list

def main():
    try:
        original_list = [2, 4, 6, 8, 10]
        new_list = insert_none(original_list)

        print("Original List:", original_list)
        print("New List with None:", new_list)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()