# Stwórz własną implementację kolejki FIFO.
# Klasa kolejka (Queue) powinna na starcie przyjmować listę elementów.
# Wśród metod powinny się znaleźć takie jak: wyswietlenie kolejki,
# sprawdzenie czy jest pusta, dodanie elementu do kolejki (put), wyjęcie elementu z kolejki (get).

class Queue():
    def __init__(self, fifo):
        self.fifo = fifo

    def show(self):
        print(self.fifo)

    def empty(self):
        return len(self.fifo) == 0

    def put(self, number):
        self.fifo.append(number)
        print(f'Dodano element {number} do kolejki')

    def get(self):
        number = self.fifo.pop(0)
        return number

def main():
    kolejka = Queue([2, 4, 6, 8, 10])
    # kolejka = Queue([])
    kolejka.show()
    # print('Do listy zostały dodane liczby 3, 6, 9')
    kolejka.put(3)
    kolejka.put(6)
    kolejka.put(9)
    kolejka.put(12)
    kolejka.show()
    print('wyjęcie pierwszego elementu z kolejki')
    print(kolejka.get())
    kolejka.show()

if __name__ == '__main__':
    main()