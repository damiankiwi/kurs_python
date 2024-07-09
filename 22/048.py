def starts_with_vowel(name):
    return name[0].upper() in 'AEIOU'

def filter_names_starting_with_vowel(names):
    return list(filter(starts_with_vowel, names))

names = ['Alice', 'Bob', 'Eve', 'Oscar', 'Uma', 'Ian', 'Charlie', 'Oliver', 'Xander']
filtered_names = filter_names_starting_with_vowel(names)
print(f"Names starting with a vowel: {filtered_names}")