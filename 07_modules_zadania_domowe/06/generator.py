import random

def main():
    x = range(10)
    y = random.choices(x, k=10)
    additional_number = random.choice(y)
    y.append(int(additional_number))
    print(y)

def instance_generator():
    x = input("Podaj 4 znaki: ")
    y = [random.choice(x) for _ in range(10)]
    return ''.join(y)

if __name__ == "__main__":
    main()