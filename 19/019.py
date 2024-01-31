def podziel_napis(s):
    if ' ' in s:
        return s.split()
    elif ',' in s:
        return s.split(',')
    else:
        return [litera.lower() for litera in s if litera.isalpha() and ord(litera) % 2 != 0]

input1 = "a b c d"
output1 = podziel_napis(input1)
print(f"Wejście:\n{input1}\nWyjście:\n{output1}")

input2 = "a,b,c,d"
output2 = podziel_napis(input2)
print(f"\nWejście:\n{input2}\nWyjście:\n{output2}")

input3 = "abcd"
output3 = podziel_napis(input3)
print(f"\nWejście:\n{input3}\nWyjście:\n{output3}")