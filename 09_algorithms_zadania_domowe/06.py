def generate_pascal_triangle(n):
    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle

def display_pascal_triangle(triangle):
    max_width = len(' '.join(str(num) for num in triangle[-1]))

    for row in triangle:
        row_str = ' '.join(str(num) for num in row)
        row_str = row_str.center(max_width)
        print(row_str)

N = int(input("Podaj wartość N:"))
pascal_triangle = generate_pascal_triangle(N)
display_pascal_triangle(pascal_triangle)