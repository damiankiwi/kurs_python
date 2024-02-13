def is_palindrome(number):
    return str(number) == str(number)[::-1]

def even_palindromes_up_to_n(n):
    even_palindromes = [i for i in range(n + 1) if i % 2 == 0 and is_palindrome(i)]
    return even_palindromes

ranges = [50, 100, 500, 2000]

for r in ranges:
    palindromes_list = even_palindromes_up_to_n(r)
    print(f"Even palindromes up to {r} -\n{palindromes_list}")