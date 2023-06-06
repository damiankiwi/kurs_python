from generator import instance_generator


def find_longest_sequence(string):
    longest_sequence = ""
    current_sequence = ""
    print(string)

    for char in string:
        if not current_sequence or char == current_sequence[-1]:
            current_sequence += char
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
            current_sequence = char

    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence

    return longest_sequence, len(longest_sequence)


def main():
    var = instance_generator()
    longest_sequence, sequence_length = find_longest_sequence(var)
    print(f"Najdłuższa sekwencja: '{longest_sequence}', Długość sekwencji: {sequence_length}")


if __name__ == "__main__":
    main()