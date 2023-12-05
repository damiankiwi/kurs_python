def find_combinations(n):
    count = 0
    for p in range(1001):
        for q in range(1001):
            for r in range(1001):
                for s in range(1001):
                    if p + q + r + s == n:
                        count += 1
    return count

def main():
    try:
        while True:
            user_input = input("Podaj dodatnią liczbę całkowitą (Wpisz 'exit', aby zakończyć): ")
            if user_input.lower() == 'exit':
                break
            user_input = int(user_input)
            if user_input <= 4000:
                result = find_combinations(user_input)
                print(f"Liczba kombinacji p, q, r, s dla {user_input}: {result}")
            else:
                print("Liczba powinna być mniejsza lub równa 4000.")
    except EOFError:
        pass

if __name__ == "__main__":
    main()
