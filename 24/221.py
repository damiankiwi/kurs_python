from bisect import bisect, bisect_left
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        top = [
            0,
            nums[-1],
            nums[-1] + nums[-2]
        ]
        min_diff = float('inf')
        three_sum = 0

        def closest(curr_target, curr_n, lo=0):
            if curr_n == 0:
                nonlocal min_diff, three_sum
                if abs(curr_target) < min_diff:
                    min_diff = abs(curr_target)
                    three_sum = target - curr_target
                return

            next_n = curr_n - 1
            max_i = len(nums) - curr_n
            max_i = bisect(
                nums, curr_target // curr_n,
                lo, max_i)
            min_i = bisect_left(
                nums, curr_target - top[next_n],
                lo, max_i) - 1
            min_i = max(min_i, lo)

            for i in range(min_i, max_i + 1):
                if min_diff == 0:
                    return
                if i == min_i or nums[i] != nums[i - 1]:
                    next_target = curr_target - nums[i]
                    closest(next_target, next_n, i + 1)

        closest(target, 3)
        return three_sum

s = Solution()
nums = [1, 2, 3, 4, 5, -6]
target = 14
result = s.threeSumClosest(nums, target)
print("\nArray values & target value:",nums,"&",target)
print("Sum of the integers closest to target:", result)

nums = [1, 2, 3, 4, -5, -6]
target = 5
result = s.threeSumClosest(nums, target)
print("\nArray values & target value:",nums,"&",target)
print("Sum of the integers closest to target:", result)