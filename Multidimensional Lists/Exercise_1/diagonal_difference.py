rows = int(input())
matrix = [[int(x) for x in input().split()]for i in range(rows)]
primary_diagonal, secondary_diagonal = [], []

for row in range(rows):
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][rows - row - 1])

print(abs(sum(primary_diagonal)- sum(secondary_diagonal)))