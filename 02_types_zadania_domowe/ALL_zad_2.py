# Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
# Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

txt = input("Proszę o wpisanie dowolnego tekstu --> ")

for i in txt[1::2]:
    print(i)

print(txt[1::2])
