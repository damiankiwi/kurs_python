def najdluzszy_wspolny_koniec(ciag1, ciag2):
    i = 1
    while i <= min(len(ciag1), len(ciag2)) and ciag1[-i:] == ciag2[-i:]:
        i += 1
    return ciag1[-(i-1):]

str1 = "running"
str2 = "ruminating"
print("Oryginalne ciągi:", str1, str2)
print("Najdłuższy wspólny koniec między tymi dwoma ciągami:", najdluzszy_wspolny_koniec(str1, str2))

str3 = "thisisatest"
str4 = "testing123testing"
print("Oryginalne ciągi:", str3, str4)
print("Najdłuższy wspólny koniec między tymi dwoma ciągami:", najdluzszy_wspolny_koniec(str3, str4))