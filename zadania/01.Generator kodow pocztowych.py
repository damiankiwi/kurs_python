def generator_kodow(start, end):
    start = int(start[:2] + start[3:])
    end = int(end[:2] + end[3:])
    wynik = []
    while start <= end:
        kod = str(start)
        wynik.append(kod[:2] + "-" + kod[2:])
        start += 1
    return wynik

print(generator_kodow("79-900", "80-155"))