import itertools


def mixed_case_combinations(input_str):
    chars = [(char.lower(), char.upper()) for char in input_str]

    all_combinations = itertools.product(*chars)

    result = [''.join(combination) for combination in all_combinations]

    return result


input_string = "a1b"
combinations = mixed_case_combinations(input_string)
print(combinations)