def main():
    original_frozenset = frozenset([1, 2, 3, 4, 5, 6])

    try:
        modified_frozenset = original_frozenset.add(7)
    except AttributeError:
        print("It is not possible to add an element to a frozenset!")

    try:
        modified_frozenset = original_frozenset.remove(2)
    except AttributeError:
        print("It is not possible to remove an element from a frozenset!")

if __name__ == "__main__":
    main()