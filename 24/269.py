def check_disjoint(frozenset_a, frozenset_b):
    return frozenset_a.isdisjoint(frozenset_b)

def main():
    frozenset_1 = frozenset([1, 2, 3, 4, 5])
    frozenset_2 = frozenset([6, 7, 8])
    print("Original frozensets:")
    print(frozenset_1)
    print(frozenset_2)
    disjoint_result1 = check_disjoint(frozenset_1, frozenset_2)
    if disjoint_result1:
        print("The frozensets are disjoint.")
    else:
        print("The frozensets are not disjoint.")
    frozenset_3 = frozenset([1, 2, 3, 4])
    frozenset_4 = frozenset([4, 5, 6, 7, 8])
    print("\nOriginal frozensets:")
    print(frozenset_3)
    print(frozenset_4)
    disjoint_result2 = check_disjoint(frozenset_3, frozenset_4)
    if disjoint_result2:
        print("The frozensets are disjoint.")
    else:
        print("The frozensets are not disjoint.")

if __name__ == "__main__":
    main()