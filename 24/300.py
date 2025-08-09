from collections import Counter

def jaccard_similarity(list1, list2):
    counter1 = Counter(list1)
    counter2 = Counter(list2)

    intersection_count = sum((counter1 & counter2).values())
    union_count = sum((counter1 | counter2).values())

    jaccard_coefficient = intersection_count / union_count
    return jaccard_coefficient

def main():
    list1 = ['Red', 'Green', 'Blue', 'Orange']
    list2 = ['Green', 'Pink', 'Blue']

    jaccard_coefficient = jaccard_similarity(list1, list2)
    print("List 1:", list1)
    print("List 2:", list2)
    print("Jaccard Similarity Coefficient:", jaccard_coefficient)

if __name__ == "__main__":
    main()