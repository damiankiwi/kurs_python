def longest_item(*args):
    return max(args, key=len)

print(longest_item('Red', 'Green', 'Black', 'Orange'))
print(longest_item([1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]))
print(longest_item([1, 2, 3], 'Java'))
print(longest_item({10, 100}, 'Python'))