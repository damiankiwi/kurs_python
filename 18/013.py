string_maps = {
    "1": "abc",
    "2": "def",
    "3": "ghi",
    "4": "jkl",
    "5": "mno",
    "6": "pqrs",
    "7": "tuv",
    "8": "wxy",
    "9": "z"
}

def generate_two_letter_combinations(digits):
    if not digits:
        return []

    def backtrack(combination, remaining_digits):
        if len(combination) == 2:
            result.append(combination)
            return

        if not remaining_digits:
            return

        current_digit = remaining_digits[0]
        for letter in string_maps[current_digit]:
            backtrack(combination + letter, remaining_digits[1:])

    result = []
    backtrack("", digits)
    return result

input_digits = "123"
combinations = generate_two_letter_combinations(input_digits)
print(combinations)
