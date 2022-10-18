rows = int(input())
matrix = [[int(x) for x in input().split(", ")] for i in range(rows)]
flattened = [num for row in matrix for num in row]

# result = []
# for row in matrix:
#     result.extend(row)

# result = []
# [result.extend(row) for row in matrix]

print(flattened)

