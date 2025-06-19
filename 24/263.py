def main():
    frozenset_x = frozenset([1, 2, 3, 4, 5])
    frozenset_y = frozenset([0, 1, 3, 7, 8, 10])
    print("Original frozensets:")
    print(frozenset_x)
    print(frozenset_y)
    union_result = frozenset_x.union(frozenset_y)
    print("Union of two said frozensets:", union_result)
    intersection_result = frozenset_x.intersection(frozenset_y)
    print("Intersection of two said frozensets:", intersection_result)
    difference_result1 = frozenset_x.difference(frozenset_y)
    difference_result2 = frozenset_y.difference(frozenset_x)
    print("Difference of (frozenset_x - frozenset_y)", difference_result1)
    print("Difference of (frozenset_y - frozenset_x)", difference_result2)

if __name__ == "__main__":
    main()