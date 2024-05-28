sequence = "aAbBcCdDeEfFgG"

def process_characters(char):
    return (char.upper(), char.lower())

unique_characters = set(sequence)
processed_characters = list(map(process_characters, unique_characters))

uppercase_chars = [char[0] for char in processed_characters]
lowercase_chars = [char[1] for char in processed_characters]

print("Original sequence:")
print(sequence)
print("Uppercase characters:")
print(uppercase_chars)
print("Lowercase characters:")
print(lowercase_chars)