import sys

def endian_check():
    if sys.byteorder == 'big':
        return "Platforma jest big-endian."
    else:
        return "Platforma jest little-endian."

print(endian_check())