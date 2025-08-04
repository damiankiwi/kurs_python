from collections import Counter

def main():
    sentence = "Red Green Black Black Red red Orange Pink Pink Red White."

    words = sentence.split()

    word_counter = Counter(words)

    print("Words in Ascending Order:")
    sorted_words_asc = sorted(word_counter.items(), key=lambda item: item[1])
    for word, count in sorted_words_asc:
        print(f"{word}: {count}")

    print("\n")

    print("Words in Descending Order:")
    sorted_words_desc = sorted(word_counter.items(), key=lambda item: item[1], reverse=True)
    for word, count in sorted_words_desc:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()