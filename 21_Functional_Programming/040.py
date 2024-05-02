"20"
import re

original_string = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"

numbers = re.findall(r'\d+', original_string)

print("Numbers:", numbers)
print("Count:", len(numbers))