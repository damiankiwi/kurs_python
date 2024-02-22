def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_length_words(sentence):
    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    result = ' '.join(prime_words)
    return result

input1 = "The quick brown fox jumps over the lazy dog."
output1 = prime_length_words(input1)
print(f"Input:\n{input1}\nOutput:\n{output1}")

input2 = "Omicron Effect: Foreign Flights Won't Resume On Dec 15, Decision Later."
output2 = prime_length_words(input2)
print(f"\nInput:\n{input2}\nOutput:\n{output2}")