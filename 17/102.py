import subprocess

polecenie = "dir"

try:
    wynik = subprocess.check_output(polecenie, shell=True, text=True)

    print("Wynik polecenia:")
    print(wynik)

except subprocess.CalledProcessError as e:
    print("Błąd podczas wykonywania polecenia:", e)
except Exception as e:
    print("Wystąpił ogólny błąd:", str(e))
