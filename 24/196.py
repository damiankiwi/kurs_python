import heapq
class Solution(object):
    def find_Kth_Smallest(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        temp = [[False] * n for _ in range(m)]
        q = [(matrix[0][0], 0, 0)]
        ans = None
        temp[0][0] = True
        for _ in range(k):
            ans, i, j = heapq.heappop(q)
            if i + 1 < m and not temp[i + 1][j]:
                temp[i + 1][j] = True
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n and not temp[i][j + 1]:
                temp[i][j + 1] = True
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
        return ans

matrix = [
   [0, 5, 9],
   [11, 12, 13],
   [15, 17, 19]
]
k = 1
s = Solution()
result = s.find_Kth_Smallest(matrix, k)
print("First smallest element:",result)
k = 2
s = Solution()
result = s.find_Kth_Smallest(matrix, k)
print("\nSecond smallest element:",result)
k = 3
s = Solution()
result = s.find_Kth_Smallest(matrix, k)
print("\nThird smallest element:",result)