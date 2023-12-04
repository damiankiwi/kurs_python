def decompress_string(compressed_str):
    result = ""
    i = 0

    while i < len(compressed_str):
        if compressed_str[i] == '#':
            count = int(compressed_str[i+1])
            result += compressed_str[i+2] * count
            i += 3
        else:
            result += compressed_str[i]
            i += 1

    return result

compressed_str_1 = "XY#6Z1#4023"
compressed_str_2 = "#39+1=1#30"


result_1 = decompress_string(compressed_str_1)
result_2 = decompress_string(compressed_str_2)

print(f"Oryginalny tekst: {result_1}")
print(f"Oryginalny tekst: {result_2}")