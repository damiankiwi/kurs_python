def main():
    try:
        numbers = input("Podaj liczby oddzielone przecinkami: ")
        numbers = numbers.split(",")
        numbers = [float(x) for x in numbers]
        if len(numbers) < 2:
            raise ValueError("Podano za mało wartości")
        average = sum(numbers) / len(numbers)
        print("Średnia wynosi:", average)
    except ValueError as e:
        print("Wprowadzono niepoprawne wartośći. Szczegóły zostały zapisane do pliku.")
        write_to_file("ValueError: " + str(e))
    # except Exception as e:
    #     print("Wystąpił błąd. Szczegóły zostały zapisane do pliku.")
    #     write_to_file("Error: " + str(e))

def write_to_file(text):
    with open("data.txt", "a", encoding = 'utf-8') as file:
        file.write(text + "\n")

if __name__ == "__main__":
    main()