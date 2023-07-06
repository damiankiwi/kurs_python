def count_words(string):
    words = string.split()  #Dzielimy ciąg znaków na wyrazy, używając spacji jako separatora
    return len(words)  #Zwracamy liczbę wyrazów

user_input = input("Podaj ciąg znaków: ")
word_count = count_words(user_input)
print("Liczba wyrazów: ", word_count)