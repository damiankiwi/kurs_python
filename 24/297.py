from collections import Counter

def add_counters(ctr1, ctr2):
    return ctr1 + ctr2

def main():
    counter1 = Counter({'item1': 10, 'item2': 34, 'item3': 22})
    counter2 = Counter({'item1': 12, 'item2': 20, 'item3': 10})

    result_counter = add_counters(counter1, counter2)

    print("Counter 1:", counter1)
    print("Counter 2:", counter2)
    print("Sum Counter:", result_counter)

if __name__ == "__main__":
    main()