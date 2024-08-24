from datetime import date

def is_valid_gregorian_date(year, month, day):
    if not (1 <= year <= 32767):
        return False

    if not (1 <= month <= 12):
        return False

    try:
        valid_date = date(year, month, day)
        return True
    except ValueError:
        return False

print(is_valid_gregorian_date(2024, 2, 29))
print(is_valid_gregorian_date(2023, 2, 29))
print(is_valid_gregorian_date(32767, 12, 31))
print(is_valid_gregorian_date(32768, 1, 1))
print(is_valid_gregorian_date(2023, 13, 1))
print(is_valid_gregorian_date(2023, 4, 31))