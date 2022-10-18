rows, columns = map(int, input().split())
matrix = []
n = 97

for row in range(rows):
    matrix.append([])
    for col in range(columns):
        matrix[row].append(chr(n + row) + chr(n + row + col) + chr(n + row))

for n in range(len(matrix)):
    print(' '.join(map(str, matrix[n])))

