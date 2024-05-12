input_string = "W3resource"

check_conditions = lambda s: any(c.isupper() for c in s) and any(c.islower() for c in s) and any(c.isdigit() for c in s) and len(s) >= 8

result = ['Valid string.'] if check_conditions(input_string) else ['Invalid string.']

print(result)