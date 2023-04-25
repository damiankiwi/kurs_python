"""Do zmiennej quote przypisz zdanie:
„Honesty is the first chapter in the book of wisdom.”, a następnie:"""

quote = "Honesty is the first chapter in the book of wisdom."

#Policz wszystkie znaki w napisie
ilosc_liter = len(quote)
print("Ilość znaków w zdaniu", ilosc_liter)

#Nie modyfikując zmiennej wyświetl słowo wisdom
print(quote[-7:-1])

#Wyświetl tylko pierwszą połowę tekstu
ilosc_liter = len(quote)
string1 = slice(0, len(quote)//2)
print(quote[string1])

#Wyświetl tylko kropkę
print(quote[-1:])

#Wyświetl od połowy tylko co trzecią literę cytatu
string2 = slice(len(quote)//2, len(quote))

"""print(quote[string2])""" #tekst od polowy
print((quote[string2])[2::3])

#Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
quote2 = "Hnsyi h is hpe ntebo fwso."
print(quote2)

#Wyświetl cały cytat odwrotnie
print((quote)[::-1])

#Zamień wisdom na słowo friendship
print(quote.replace('wisdom', 'friendship'))
