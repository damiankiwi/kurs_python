class Mammals:
    def __init__(self, name, fur_color=""):
        self.name = name
        self.fur_color = fur_color

    def description(self):
        if self.name.lower() == "ssaki":
            print("Ssaki to zwierzęta, które karmią swoje młode mlekiem matki, ich ciało zwykle jest pokryte włosami.")
        else:
            print(f"{self.name}, zwierzę należące do gromady ssaków.")

    def feeding(self):
        print(f"{self.name}, karmi potmostwo mlekiem.")

    def fur(self):
        print(f"{self.name}, ma ciało pokryte włosami kolor {self.fur_color}.")

def main():
    ssaki = Mammals("Ssaki")
    wilk = Mammals("Wilk", "szary")
    kon = Mammals("Koń", "kasztanowy")

    ssaki.description()

    wilk.description()
    wilk.feeding()
    wilk.fur()

    kon.description()
    kon.feeding()
    kon.fur()

if __name__ == '__main__':
    main()