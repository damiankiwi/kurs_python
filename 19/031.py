import math

def find_triangle_coordinates(side_lengths):
    a, b, c = side_lengths

    def find_third_vertex(a, b, c):
        x = (c**2 - b**2 + a**2) / (2 * a)
        y = math.sqrt(c**2 - x**2)
        return [x, y]

    A = [0.0, 0.0]
    B = [a, 0.0]
    C = find_third_vertex(a, b, c)

    return [A, B, C]

input1 = [3, 4, 5]
output1 = find_triangle_coordinates(input1)
print(f"Input:\n{input1}\nOutput:\n{output1}")

input2 = [5, 6, 7]
output2 = find_triangle_coordinates(input2)
print(f"\nInput:\n{input2}\nOutput:\n{output2}")