import time

def metoda_do_mierzenia():
    total = 0
    for i in range(1000000):
        total += i

start_time = time.time()

metoda_do_mierzenia()

end_time = time.time()

execution_time = end_time - start_time

print(f"Czas wykonania metody: {execution_time:.6f} sekundy")
