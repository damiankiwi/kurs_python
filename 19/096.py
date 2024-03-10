def digits_to_words(numbers):
    digit_words = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }

    sorted_digits = sorted(set(str(num) for num in numbers if 0 <= num <= 9), reverse=True)
    result = [digit_words[int(digit)] for digit in sorted_digits]

    return result

input_numbers1 = [1, 3, 4, 5, 11]
output1 = digits_to_words(input_numbers1)
print(f"Output 1: {output1}")

input_numbers2 = [27, 3, 8, 5, 1, 31]
output2 = digits_to_words(input_numbers2)
print(f"Output 2: {output2}")