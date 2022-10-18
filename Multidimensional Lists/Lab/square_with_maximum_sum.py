rows, columns = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split(', ')] for i in range(rows)]

total = 0
final_matrix = []
for row in range(rows - 1):
    for col in range(columns - 1):
        if rows - 1 >= 0 and columns - 1 >= 0:
            a = matrix[row][columns - col - 1]
            b = matrix[row][columns - col - 2]
            c = matrix[row + 1][columns - col - 1]
            d = matrix[row + 1][columns - col - 2]

            total_sum = a + b + c + d
            if total_sum > total:
                total = total_sum
                final_matrix = [b, a], [d, c]
            elif total_sum == total:
                if ma


for r in range(len(final_matrix)):
    print(' '.join(map(str, final_matrix[r])))

print(total)
