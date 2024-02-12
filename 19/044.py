def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def hex_chars_prime(hex_number):
    result = [is_prime(int(char, 16)) for char in hex_number]
    return result

input_hex1 = "123ABCD"
output1 = hex_chars_prime(input_hex1)
print(f"Input: {input_hex1}")
print(f"Output: {output1}")

input_hex2 = "123456"
output2 = hex_chars_prime(input_hex2)
print(f"\nInput: {input_hex2}")
print(f"Output: {output2}")

input_hex3 = "FACE"
output3 = hex_chars_prime(input_hex3)
print(f"\nInput: {input_hex3}")
print(f"Output: {output3}")