import sys

nazwa_skryptu = sys.argv[0]

liczba_argumentow = len(sys.argv) - 1

argumenty = sys.argv[1:]

print("Nazwa skryptu:", nazwa_skryptu)
print("Liczba argumentów:", liczba_argumentow)
print("Argumenty:", argumenty)
