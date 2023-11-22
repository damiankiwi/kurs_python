input_numbers = input("Podaj sześć liczb całkowitych oddzielonych spacją: ")

numbers_list = [int(num) for num in input_numbers.split()]

numbers_list.sort(reverse=True)

print("Po posortowaniu wprowadzonych liczb:")
print(" ".join(map(str, numbers_list)))