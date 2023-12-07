def najdluzsze_slowo_podciag(slowo, podciagi):
    najdluzsze = ""
    for podciag in podciagi:
        i, j = 0, 0
        while i < len(slowo) and j < len(podciag):
            if slowo[i] == podciag[j]:
                j += 1
            i += 1
        if j == len(podciag) and len(podciag) > len(najdluzsze):
            najdluzsze = podciag
    return najdluzsze

input1 = ("Green", {"Gn", "Gren", "ree", "en"})
input2 = ("pythonexercises", {"py", "ex", "exercises"})

output1 = najdluzsze_slowo_podciag(*input1)
output2 = najdluzsze_slowo_podciag(*input2)

print(output1)
print(output2)