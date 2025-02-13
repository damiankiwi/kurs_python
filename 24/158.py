def pigeonhole_sort(a):
    min_val = min(a)
    max_val = max(a)
    size = max_val - min_val + 1
    holes = [0] * size
    for x in a:
        assert isinstance(x, int), "integers only please"
        holes[x - min_val] += 1
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            a[i] = count + min_val
            i += 1

nums = [4, 3, 5, 1, 2]
print("\nOriginal list:")
print(nums)
pigeonhole_sort(nums)
print("Sorted order is:", nums)
nums = [5, 9, 10, 3, -4, 5, 178, 92, 46, -18, 0, 7]
print("\nOriginal list:")
print(nums)
pigeonhole_sort(nums)
print("Sorted order is:", nums)