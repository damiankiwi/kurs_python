import itertools

def infinite_iterator(start, step):
    return itertools.count(start=start, step=step)

start_value = 10
step_value = 2

iterator = infinite_iterator(start_value, step_value)

print("First 10 values from the infinite iterator:")
for _ in range(10):
    print(next(iterator))