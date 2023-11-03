X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
target = 70

combinations = []

for x in X:
    for y in Y:
        for z in Z:
            if x + y + z == target:
                combinations.append((x, y, z))

print(f"Kombinacje trzech elementów sumujące się do {target}:")
for combo in combinations:
    print(combo)
