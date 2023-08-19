import subprocess

try:
    komenda = input("Podaj komendę do wykonania: ")
    wynik = subprocess.run(komenda, shell=True, capture_output=True, text=True)

    print("Standardowe wyjście:")
    print(wynik.stdout)

    print("Błędy standardowe:")
    print(wynik.stderr)
except subprocess.CalledProcessError:
    print("Wystąpił błąd podczas wywoływania komendy.")
