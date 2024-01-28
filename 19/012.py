def sprawdz_palindromy(lista):
    wyniki = [slowo == slowo[::-1] for slowo in lista]
    return wyniki

input_strings = ['palindrome', 'madamimadam', '', 'foo', 'eyes']
output_results = sprawdz_palindromy(input_strings)
print(f"Input:\n{input_strings}\nOutput:\n{output_results}")