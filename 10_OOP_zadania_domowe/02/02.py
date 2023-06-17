class Orchid:
    plant_kingdom = "Rosliny"

    def __init__(self, color, flowering_season, species):
        self.color = color
        self.flowering_season = flowering_season
        self.species = species

    def description(self):
        print(f"Storczyk: {self.species}")
        print(f"Kolor: {self.color}")
        print(f"Pora kwitnienia: {self.flowering_season}")

    def water(self):
        print("Watering the orchid...")

orchid1 = Orchid("white", "summer", "Phalaenopsis")
orchid1.description()
orchid1.water()

orchid2 = Orchid("purple", "spring", "Cattleya")
orchid2.description()
orchid2.water()