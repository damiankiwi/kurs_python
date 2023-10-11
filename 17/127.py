import sys

def jaka_liczba_miesci_sie_w_64_bitach(liczba):
    rozmiar_w_bajtach = sys.getsizeof(liczba)
    rozmiar_w_bitach = rozmiar_w_bajtach * 8
    return rozmiar_w_bitach, "int64" if rozmiar_w_bitach == 64 else "poza zakresem int64"

przykladowa_liczba = 9223372036854775807  # To jest maksymalna liczba 64-bitowa

rozmiar, rodzaj = jaka_liczba_miesci_sie_w_64_bitach(przykladowa_liczba)

if rodzaj == "int64":
    print("Liczba", przykladowa_liczba, "mieści się w 64 bitach jako", rodzaj, "i zajmuje", rozmiar, "bitów.")
else:
    print("Liczba", przykladowa_liczba, "nie mieści się w 64 bitach. Rozmiar:", rozmiar, "bitów, rodzaj:", rodzaj)
