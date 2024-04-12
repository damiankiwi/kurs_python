def is_in_range(number, start, end):
    return start <= number < end

number = 5
start = 1
end = 10
if is_in_range(number, start, end):
    print(number, "falls within the range from", start, "to", end)
else:
    print(number, "does not fall within the range from", start, "to", end)