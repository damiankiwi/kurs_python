def main():
    nums = [1, 1, 2, 3, 2, 4, 5, 5, 6, 7, 7]

    unique_frozenset_nums = frozenset(nums)

    print("Original List:", nums)
    print("Unique Frozenset:", unique_frozenset_nums)

if __name__ == "__main__":
    main()