import time

czas_poczatkowy = time.time()

time.sleep(3)

czas_aktualny = time.time()

czas_dzialania = czas_aktualny - czas_poczatkowy

print("Czas działania programu wynosi:", czas_dzialania, "sekund")
