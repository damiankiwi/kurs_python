def stooge_sort(arr):
    stooge(arr, 0, len(arr) - 1)
    return arr
def stooge(arr, i, h):
    if i >= h:
        return
    if arr[i] > arr[h]:
        arr[i], arr[h] = arr[h], arr[i]
    if h - i + 1 > 2:
        t = (int)((h - i + 1) / 3)
        stooge(arr, i, (h - t))
        stooge(arr, i + t, (h))
        stooge(arr, i, (h - t))
lst = [4, 3, 5, 1, 2]
print("\nOriginal list:")
print(lst)
print("After applying  Stooge sort the said list becomes:")
print(stooge_sort(lst))
lst = [5, 9, 10, 3, -4, 5, 178, 92, 46, -18, 0, 7]
print("\nOriginal list:")
print(lst)
print("After applying Stooge sort the said list becomes:")
print(stooge_sort(lst))
lst = [1.1, 1, 0, -1, -1.1, .1]
print("\nOriginal list:")
print(lst)
print("After applying Stooge sort the said list becomes:")
print(stooge_sort(lst))