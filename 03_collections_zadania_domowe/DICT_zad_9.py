#9. 5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty
# powtarzają się na listach. Wyświetl najpopularniejszy przedmiot. (Uwzględnij fakt,
# że użytkownicy mogą zapisać przedmioty małymi, drukowanymi lub zaczynając od dużej litery)

school_subjects = []

for i in range(5):
    print(f'Uczeń {i + 1} Podaj 4 przedmioty szkolne')
    for j in range(4):
        i = input(f'Witaj podaj {j + 1} przedmiot: ')
        i = i.format(j + 1).lower().capitalize()
        school_subjects.append(i)
# print('Wszystkie przedrmioty wymienione przez uczniów: ', subjects)

counting = {}
for subject in school_subjects:
    if subject in counting:
        counting[subject] = counting[subject] + 1
    else:
        counting[subject] = 1

for k, v in counting.items():
    print(k, ':', v)

number_occurrences = [value for [key, value] in counting.items()]
high_occurrences = max(number_occurrences)

for key, value in counting.items():
    if counting[key] == high_occurrences:
        print(f'Najczesciej wymienieniany przedmiot', key, 'wystapił', high_occurrences, 'razy.')
