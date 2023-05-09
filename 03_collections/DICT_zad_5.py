# 5. W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.

poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

# print(poem)

poem = poem.lower()
poem = poem.replace(",", "")
words = poem.split()

#poem = poem.lower().replace(",", "").split()

counting = {}
for word in words:
    if word in counting:
        counting[word] = counting[word] + 1
        # counting[word] += 1
    else:
        counting[word] = 1

for k, v in counting.items():
    print(k, ':', v)
