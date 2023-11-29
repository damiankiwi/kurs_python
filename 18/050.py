text = input("Podaj tekst zawierający słowa 'Python' i 'Java': ")

text = text.replace("Python", "JavaTemp")
text = text.replace("Java", "Python")
text = text.replace("JavaTemp", "Java")

print(text)