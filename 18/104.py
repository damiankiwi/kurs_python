def znajdz_max_w_kolumnie_min_w_wierszu(matrix):
    result = []

    for i in range(len(matrix)):
        min_in_row = min(matrix[i])
        col_index = matrix[i].index(min_in_row)

        is_max_in_column = all(matrix[j][col_index] <= matrix[i][col_index] for j in range(len(matrix)))

        if is_max_in_column:
            result.append(matrix[i][col_index])

    return result

matrix1 = [[1, 2], [2, 3]]
matrix2 = [[1, 2, 3], [3, 4, 5]]
matrix3 = [[7, 5, 6], [3, 4, 4], [6, 5, 7]]

wynik1 = znajdz_max_w_kolumnie_min_w_wierszu(matrix1)
wynik2 = znajdz_max_w_kolumnie_min_w_wierszu(matrix2)
wynik3 = znajdz_max_w_kolumnie_min_w_wierszu(matrix3)

print(f"Macierz: {matrix1}\nLiczba, która jest maksymalna w kolumnie i minimalna w wierszu: {wynik1}")
print(f"Macierz: {matrix2}\nLiczba, która jest maksymalna w kolumnie i minimalna w wierszu: {wynik2}")
print(f"Macierz: {matrix3}\nLiczba, która jest maksymalna w kolumnie i minimalna w wierszu: {wynik3}")