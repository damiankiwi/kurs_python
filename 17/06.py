def main():
    sequence = input("Podaj sekwencję liczb oddzielonych przecinkami: ")

    numbers_list = sequence.split(',')
    numbers_list = [num.strip() for num in numbers_list]

    numbers_tuple = tuple(numbers_list)

    print("List : ", numbers_list)
    print("Tuple : ", numbers_tuple)

if __name__ == "__main__":
    main()