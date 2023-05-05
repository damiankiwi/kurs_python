# 1▹ Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi).
# Następnie rozpakuj tę krotkę na pojedyńcze zmienne. Wykorzystaj zmienne do wyświetlenia
# f-stringa, tak by mogło powstać zdanie np. “Mój pies, rasy border collie wabi się Dyzio”.


pet_info = ('kot', 'dachowiec', 'Beza')

(type_animal, race, name) = pet_info

print(f'Mój {type_animal}, rasy {race} wabi się {name}.')
