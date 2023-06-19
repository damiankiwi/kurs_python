def binary_search(elem, data):
    data.sort()
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if data[mid] == elem:
            return f"Liczba {elem} jest na liście"
        elif data[mid] < elem:
            left = mid + 1
        else:
            right = mid - 1

    return f"Liczba {elem} nie jest na liście"

data = [3, 15, 45, 2, 6, 12, 44, 34, 21, 56, 7, 3, 12]
elem = 21

result = binary_search(elem, data)
print(result)
