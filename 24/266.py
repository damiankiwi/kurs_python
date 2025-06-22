def powerset(frozenset_input):
    power_set = [[]]

    for element in frozenset_input:
        new_subsets = []
        for subset in power_set:
            new_subset = subset + [element]
            new_subsets.append(new_subset)
        power_set.extend(new_subsets)

    return [frozenset(subset) for subset in power_set]

def main():
    frozen_set = frozenset([1, 2, 3, 4])
    print("Original Power set")

    power_set_result = powerset(frozen_set)

    print("Power Set:")
    for subset in power_set_result:
        print(subset)

if __name__ == "__main__":
    main()