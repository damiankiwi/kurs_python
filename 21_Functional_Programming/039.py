from collections import Counter

strings = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
target = 'abcd'

anagrams = list(filter(lambda x: Counter(x) == Counter(target), strings))

print("Anagrams of '{}' in the above string:".format(target))
print(anagrams)