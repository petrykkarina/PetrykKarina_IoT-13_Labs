import numpy as np

matrix = [
    [33, -5, -9, -20, -11],
    [0, -42, 86, 83, 71],
    [-6, -9, 33, 13, 22],
    [52, -5, -7, 53, 19],
    [-3, 98, 72, 68, 0]
]

def selection_sort_desc(row):
    for i in range(len(row)):
        max_index = i
        for j in range(i + 1, len(row)):
            if row[j] > row[max_index]:
                max_index = j
        row[i], row[max_index] = row[max_index], row[i]
    return row

sorted_matrix = [selection_sort_desc(row.copy()) for row in matrix]

def calculate_column_averages(matrix):
    n = len(matrix)
    m = len(matrix[0])
    averages = []
    for col in range(m):
        elements = []
        for row in range(n):
            if row + col < m - 1:  
                elements.append(matrix[row][col])
        if elements:
            averages.append(sum(elements) / len(elements))
    return averages

averages = calculate_column_averages(sorted_matrix)

def calculate_F(averages):
    F = 1
    for avg in averages:
        F *= avg
    return F

F_result = calculate_F(averages)

print("Відсортована матриця:")
for row in sorted_matrix:
    print(row)

print("\nЗначення f_i(a_ij) для кожного стовпця над допоміжною діагоналлю:")
print(averages)

print("\nЗначення функції F(f_i(a_ij)):")
print(F_result)
