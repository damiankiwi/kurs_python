from fibonacci import fibonacci_sequence


def main():
    n = int(input('Podaj wartość aby stworzyć ciąg fibbonaciego:'))
    result = fibonacci_sequence(n)
    print(result)

if __name__ == "__main__":
    main()
