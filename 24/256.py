import numpy as np

nums = np.array([2, 4, 6, 8, 10], dtype=np.int32)

memory_view = memoryview(nums)

total = 0
for element in memory_view:
    total += element
average = total / len(memory_view)
print("NumPy Array:", nums)
print("Memory View:", memory_view)
print("Average:", average)