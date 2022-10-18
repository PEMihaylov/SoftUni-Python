rows, columns = [int(x) for x in input().split(", ")]
matrix = []

for row in range(rows):
    elements = [int(x) for x in input().split(", ")]
    matrix.append(elements)

total = 0
# for i in range(rows):
#     total += sum(matrix[i])

for row in range(rows):
    for col in range(columns):
        total += matrix[row][col]

print(total)
print(matrix)