import random
from collections import OrderedDict

def  random_ascii():
    return chr(random.randint(65, 90))

def main():
    ordered_dict = OrderedDict()

    for _ in range(10):
        key = random_ascii()
        value = random.randint(1, 50)
        ordered_dict[key] = value

    print("OrderedDict:", ordered_dict)

if __name__ == "__main__":
    main()