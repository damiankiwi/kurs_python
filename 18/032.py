
heights = []
for i in range(8):
    height = int(input("Podaj wysokość budynku {}: ".format(i + 1)))
    heights.append(height)

sorted_heights = sorted(heights, reverse=True)

top_three = sorted_heights[:3]

print("Wysokości trzech najwyższych budynków w porządku malejącym:")
for height in top_three:
    print(height)