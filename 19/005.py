def sprawdz_podciag(lista):
    for i in range(1, len(lista)):
        if lista[i-1] not in lista[i]:
            return False
    return True

print(sprawdz_podciag(['a', 'abb', 'sfs', 'oo', 'de', 'sfde']))
print(sprawdz_podciag(['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']))
print(sprawdz_podciag(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']))
print(sprawdz_podciag(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']))