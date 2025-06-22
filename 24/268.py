def main():
    nums = [1, 1, 2, 3, 2, 4, 5, 5, 6, 7, 7]
    unique_frozenset_nums = frozenset(nums)

    nums1 = [1, 1, 3, 3, 2, 5, 5, -7, -7, 6, 0]
    unique_frozenset_nums1 = frozenset(nums1)

    print("Original List:", nums)
    print("Unique Frozenset:", unique_frozenset_nums)

    print("Original List:", nums1)
    print("Unique Frozenset:", unique_frozenset_nums1)

if __name__ == "__main__":
    main()