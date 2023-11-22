x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input("Podaj x1, y1, x2, y2, x3, y3, x4, y4 oddzielone spacją: ").split())

if (y2 - y1) * (x4 - x3) == (y4 - y3) * (x2 - x1):
    print("Odcinki PQ i RS są równoległe")
else:
    print("Odcinki PQ i RS nie są równoległe")