def sort_hyphen_separated_sequence(sequence):
    words = sequence.split('-')

    sorted_words = sorted(words)

    sorted_sequence = '-'.join(sorted_words)

    return sorted_sequence

sample_items = "green-red-yellow-black-white"
sorted_sequence = sort_hyphen_separated_sequence(sample_items)
print("Sorted Sequence:", sorted_sequence)