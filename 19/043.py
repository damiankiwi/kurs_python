def count_consonants(word):
    return sum(1 for char in word.lower() if char.isalpha() and char not in 'aeiou')

def words_with_n_consonants(input_str, n):
    words = input_str.split()
    result = {i: [] for i in range(1, n + 1)}

    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count <= n:
            result[consonant_count].append(word)

    return result

input_str = "this is our time"
max_consonants = 3
for i in range(1, max_consonants + 1):
    result = words_with_n_consonants(input_str, i)
    print(f"Number of consonants: {i}")
    print(f"Words in the said string with {i} consonant(s):")
    print(result[i])
    print()