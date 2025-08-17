import numpy as np

def slice_third_dimension(arr):
    return arr[..., :2]

nums = np.array([[[1, 2, 3], [4, 5, 6]],
                           [[7, 8, 9], [10, 11, 12]],
                           [[13, 14, 15], [16, 17, 18]]])
print("Original multidimensional array:")
print(nums)

sliced_array = slice_third_dimension(nums)
print("\nSlices the first two elements from the said array:")
print(sliced_array)