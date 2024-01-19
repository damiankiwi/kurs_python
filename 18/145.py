def znajdz_najwieksza_i_najmniejsza_cyfre(liczba):
    liczba_str = str(liczba)
    najwieksza_cyfra = najmniejsza_cyfra = int(liczba_str[0])

    for cyfra_str in liczba_str:
        cyfra = int(cyfra_str)

        if cyfra > najwieksza_cyfra:
            najwieksza_cyfra = cyfra

        if cyfra < najmniejsza_cyfra:
            najmniejsza_cyfra = cyfra

    return najwieksza_cyfra, najmniejsza_cyfra

liczba1 = 9387422
najwieksza1, najmniejsza1 = znajdz_najwieksza_i_najmniejsza_cyfre(liczba1)
print("Oryginalna Liczba:", liczba1)
print("Największa Cyfra w danej liczbie:", najwieksza1)
print("Najmniejsza Cyfra w danej liczbie:", najmniejsza1)

liczba2 = 500
najwieksza2, najmniejsza2 = znajdz_najwieksza_i_najmniejsza_cyfre(liczba2)
print("Oryginalna Liczba:", liczba2)
print("Największa Cyfra w danej liczbie:", najwieksza2)
print("Najmniejsza Cyfra w danej liczbie:", najmniejsza2)

liczba3 = 231548
najwieksza3, najmniejsza3 = znajdz_najwieksza_i_najmniejsza_cyfre(liczba3)
print("Oryginalna Liczba:", liczba3)
print("Największa Cyfra w danej liczbie:", najwieksza3)
print("Najmniejsza Cyfra w danej liczbie:", najmniejsza3)