xp, yp, xq, yq, xr, yr, xs, ys = map(float, input("Podaj współrzędne punktów P, Q, R, S (xp, yp, xq, yq, xr, yr, xs, ys): ").split())

wektor_ab = ((xq - xp), (yq - yp))
wektor_cd = ((xs - xr), (ys - yr))

iloczyn_skalarny = wektor_ab[0] * wektor_cd[0] + wektor_ab[1] * wektor_cd[1]

if iloczyn_skalarny == 0:
    print("AB i CD są prostopadłe!")
else:
    print("AB i CD nie są prostopadłe!")