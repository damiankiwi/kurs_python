# 2.  Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.

elements = ("monitor", "myszka", "myszka", "klawiatura", "podkładka", "modem", "słuchawki", "myszka")
print(elements)
for i in elements:
    count = elements.count(i)
    if count > 1:
        print(i)


