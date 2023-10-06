
ciag_znakow = "To jest przykładowy ciąg znaków, który zostanie sformatowany i ograniczony."

maks_dlugosc = 30

if len(ciag_znakow) > maks_dlugosc:
    sformatowany_ciag = ciag_znakow[:maks_dlugosc] + "..."
else:
    sformatowany_ciag = ciag_znakow

print(sformatowany_ciag)
