import heapq
from collections import Counter
class Solution:
    def top_K_Frequent(self, words, k):

        ctr = Counter(words)
        heap = [(-ctr[word], word) for word in ctr]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

if __name__ == '__main__':
    words = ["a", "abc", "abcdef", "a", "abcd", "abcd", "abc", "abcdefg"]
    k = 3
    s = Solution()
    print("3 most frequent elements:")
    print(s.top_K_Frequent(words, k))