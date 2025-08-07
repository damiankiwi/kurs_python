from collections import Counter

def main():
    items = ["Red", "Green", "Black", "Black", "Red", "red", "Orange", "Pink", "Pink", "Red", "White"]
    item_counter = Counter(items)

    unique_items_with_counts = list(item_counter.items())

    print("Original List:", items)
    print("Counter:", item_counter)
    print("Unique Items with Counts:", unique_items_with_counts)

if __name__ == "__main__":
    main()