# palindorm to wyrazenie brzmiace tak samo czytane od lewej do orawej i od prawej od lewej np:
# Kobyła ma mały bok.
# Pozwól uzytkownikowi wprowadzić dowolnej zdanie.
# Następnie sprawdź czy wprowadzone wyrażenie jest palindromem

txt  = input("give me text here -> ")
txt = txt.replace(" ", "").upper()
print('Is palindrom?', txt == txt[::-1])