#8. Utwórz słownik dla 10 krajów Europy zawierajacy listy 10 najpopularniejszych imion
# żeńskich. Zapisz imiona w wersji anglojęzycznej. Dodaj wszystki listy razem.
# Nowa lista powinna zawierać 100 elementów.

#Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.
names = {
'Austria' : ['Sarah', 'Anna',	'Julia', 'Laura', 'Lena', 'Hannah', 'Lisa', 'Katharina', 'Leonie', 'Vanessa'],
'Belgium' : ['Emma', 'Marie', 'Laura', 'Julie', 'Sarah', 'Clara', 'Manon', 'Léa', 'Lisa', 'Camille'],
'Denmark' : ['Mathilde', 'Emma', 'Laura', 'Sofie', 'Freja', 'Caroline', 'Ida', 'Sara', 'Julie', 'Anna'],
'Estonia' : ['Sofia', 'Maria', 'Laura', 'Sandra', 'Lisandra', 'Milana', 'Anna', 'Viktoria', 'Emma', 'Mirtel'],
'Finland' : ['Emma', 'Ella', 'Siiri', 'Aino', 'Anni', 'Sara', 'Venla', 'Aada', 'Emilia', 'Iida'],
'France': ['Léa', 'Manon', 'Emma', 'Chloé', 'Camille', 'Océane', 'Clara', 'Marie', 'Sarah', 'Inès'],
'Germany' : ['Marie', 'Sofie', 'Maria', 'Anna', 'Leonie', 'Lena', 'Emily', 'Lea', 'Julia', 'Laura'],
'Italy' : ['Giulia', 'Sara', 'Sofia', 'Martina', 'Chiara', 'Alessia', 'Giorgia', 'Aurora', 'Francesca', 'Giada'],
'Netherlands' : ['Sanne', 'Emma', 'Anna', 'Iris', 'Anouk', 'Melissa', 'Eva', 'Julia', 'Lotte', 'Isa'],
'Poland' : ['Anna', 'Maria', 'Katarzyna', 'Małgorzata', 'Agnieszka', 'Krystyna', 'Barbara', 'Ewa', 'Elżbieta', 'Zofia'],
}
# country_dict = [Austria, Belgium, Denmark, Estonia, Finland, France, Germany, Italy, Netherlands, Poland]

names_list = []
for i, j in names.items():
    for k in j:
        names_list.append(k)
# print(names_list) # lista wszystkich imiom
names_calc = {}
for i in names_list:
    if i in names_calc:
        names_calc[i] += 1
    else:
        names_calc[i] = 1
# print(names_calc) #zliczanie imion
print('Imiona które wystąpiły conajmniej w 3 krajach to: ')
for k, v in names_calc.items():
    if v >= 3:
        print(k, end=" ")