from itertools import permutations

def is_valid_time(hours, minutes):
    return 0 <= hours < 24 and 0 <= minutes < 60

def latest_time_from_digits(digits):
    max_time = -1
    for perm in permutations(digits):
        hours = perm[0] * 10 + perm[1]
        minutes = perm[2] * 10 + perm[3]
        if is_valid_time(hours, minutes):
            total_minutes = hours * 60 + minutes
            if total_minutes > max_time:
                max_time = total_minutes
                best_time = f"{hours:02}:{minutes:02}"
    return best_time if max_time != -1 else "No valid time"

digits = [1, 9, 5, 2]
print("Latest time:", latest_time_from_digits(digits))