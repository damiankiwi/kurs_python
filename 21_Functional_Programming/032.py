array = [-1, 2, -3, 5, 7, 8, 9, -10]

rearrange = lambda arr: sorted(arr, key=lambda x: (x >= 0, x))

result = rearrange(array)

print("Rearrange positive and negative numbers of the said array:", result)