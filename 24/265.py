def symmetric_difference(frozenset_x, frozenset_y):
    return frozenset_x.symmetric_difference(frozenset_y)

def main():
    frozenset_a = frozenset([1, 2, 3, 4, 5, 6])
    frozenset_b = frozenset([4, 5, 6, 7, 8])
    print("Original frozensets:")
    print(frozenset_a)
    print(frozenset_b)
    sym_diff_result = symmetric_difference(frozenset_a, frozenset_b)
    print("\nSymmetric Difference of said two frozenset:", sym_diff_result)

if __name__ == "__main__":
    main()