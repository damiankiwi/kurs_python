import struct

def sprawdz_tryb_bitowy():
    arch = struct.calcsize("P") * 8
    return arch

tryb = sprawdz_tryb_bitowy()
print(f"Tryb bitowy: {tryb}-bit")