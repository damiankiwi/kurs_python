import glob

lista_plikow = glob.glob('*')

print("Lista plików w bieżącym katalogu:")
for plik in lista_plikow:
    print(plik)
