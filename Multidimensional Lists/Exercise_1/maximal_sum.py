rows, columns = map(int, input().split())

matrix = [[int(x) for x in input().split()]for i in range(rows)]
total_sum = 0
final_matrix = []

for row in range(rows - 2):
    for col in range(columns - 2):
        a = matrix[row][columns - col -1]
        b = matrix[row][columns - col -2]
        c = matrix[row][columns - col -3]
        d = matrix[row + 1][columns - col -1]
        e = matrix[row + 1][columns - col -2]
        f = matrix[row + 1][columns - col -3]
        g = matrix[row + 2][columns - col -1]
        h = matrix[row + 2][columns - col -2]
        l = matrix[row + 2][columns - col -3]
        current_sum = a + b + c + d + e + f + g + h +l
        if current_sum >= total_sum:
            total_sum = current_sum
            final_matrix = [c, b, a], [f, e, d], [l, h, g]


print(f"Sum = {total_sum}")
for r in range(len(final_matrix)):
    print(' '.join(map(str, final_matrix[r])))


