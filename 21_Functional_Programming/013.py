def pascals_triangle(n):
    def pascal_value(row, col):
        if col == 0 or col == row:
            return 1
        else:
            return pascal_value(row-1, col-1) + pascal_value(row-1, col)

    for i in range(n):
        row = [pascal_value(i, j) for j in range(i + 1)]
        print(' '.join(map(str, row)).center(n*2))

pascals_triangle(5)