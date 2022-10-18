N = int(input())

matrix = [[x for x in input()]for i in range(N)]
symbol = input()
found_sym = False

for row in range(N):
    for col in range(len(matrix[row])):
        if found_sym:
            break

        if matrix[row][col] == symbol:
            found_sym = True
            print(f"({row}, {col})")


if not found_sym:
    print(f"{symbol} does not occur in the matrix")