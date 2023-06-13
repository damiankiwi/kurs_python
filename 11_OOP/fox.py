class Fox:
    paws = 4
    ears = 2
    tail = 1
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Lis istnieje -" + self.name

    def make_sound(self, sound):
        print("Lis:", sound * 2)

lisek = Fox('Reksio')
print(lisek)
lisek.make_sound("miau")
print(lisek.paws)

