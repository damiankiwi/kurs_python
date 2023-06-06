# 1▹ Skorzystaj z wprowadzenia do OOP. Stwórz klasę Pies, która posiada wspomniane atrybuty oraz metodę.
#
# atrybuty: imię, kolor sierści, rasę
#
# metody: szczekaj, machaj ogonem
#
# Utwórz kilka obiektów klasy Pies z różnymi parametrami.

class dog:
    def __init__(self, firstname, coat_color, race):
        self.firstname = firstname
        self.coat_color = coat_color
        self.race = race

    def bark(self, number):
        return 'Hau ' * number

    def wag_your_tail(self, number):
        return 'Macha ogonem ' * number



reksio = dog('Reksio', 'biała', 'jamnik')
burek = dog('Burek', 'burasek', 'mieszaniec')
pimpek = dog('Pimpek', 'szary', 'husky')

print(reksio.bark(3))
print(burek.bark(1))
print(pimpek.wag_your_tail(5))