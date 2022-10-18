rows, columns = map(int, input().split())

matrix = [[x for x in input().split()]for j in range(rows)]
num_of_matrices = 0

for row in range(rows -1):
    for col in range(columns -1):
        p = matrix[row][columns - col -1]
        y = matrix[row][columns - col -2]
        z = matrix[row + 1][columns - col -1]
        t = matrix[row + 1][columns - col -2]
        if p == y == z == t:
            num_of_matrices += 1

print(num_of_matrices)

#....SoftUni teachers' solution

# `for row in range(len(matrix)):
#     if row == rows -1:
#         continue
#     for col in range(len(matrix[row])):
#         if col == cols -1:
#             continue
#         if matrix[row][col] == matrix[row][row + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
#             counter += 1`
