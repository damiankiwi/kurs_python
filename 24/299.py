from collections import Counter

def main():
    colors = ["Red", "Green", "Black", "Black", "Red", "red", "Orange", "Pink", "Pink", "Red", "White"]
    color_counter = Counter(colors)

    min_count = 2
    filtered_counter = {word: count for word, count in color_counter.items() if count >= min_count}

    print("Original List:", colors)
    print("Counter:", color_counter)
    print(f"Items with Count >= {min_count}:", filtered_counter)

if __name__ == "__main__":
    main()