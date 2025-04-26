from bisect import bisect_left
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        N = 4
        quadruplets = []
        if len(nums) < N:
            return quadruplets
        nums = sorted(nums)
        quadruplet = []

        top = [0]
        for i in range(1, N):
            top.append(top[i - 1] + nums[-i])

        def sum_(curr_target, curr_n, lo=0):
            if curr_n == 0:
                if curr_target == 0:
                    quadruplets.append(quadruplet[:])
                return

            next_n = curr_n - 1
            max_i = len(nums) - curr_n
            max_i = bisect_left(
                nums, curr_target // curr_n,
                lo, max_i)
            min_i = bisect_left(
                nums, curr_target - top[next_n],
                lo, max_i)

            for i in range(min_i, max_i + 1):
                if i == min_i or nums[i] != nums[i - 1]:
                    quadruplet.append(nums[i])
                    next_target = curr_target - nums[i]
                    sum_(next_target, next_n, i + 1)
                    quadruplet.pop()

        sum_(target, N)
        return quadruplets

s = Solution()
nums = [-2, -1, 1, 2, 3, 4, 5, 6]
target = 10
result = s.fourSum(nums, target)
print("\nArray values & target value:",nums,"&",target)
print("Solution Set:\n", result)