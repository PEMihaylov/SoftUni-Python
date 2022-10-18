rows, columns = map(int, input().split())
matrix = [[x for x in input().split()] for i in range(rows)]

while True:
    command = input()
    if command == "END":
        break

    inline = command.split()

    if "swap" not in inline or len(inline) != 5:
        print("Invalid input!")
        continue

    row1 = int(inline[1])
    col1 = int(inline[2])
    row2 = int(inline[3])
    col2 = int(inline[4])

    if False in [0 <= row1 < rows, 0 <= col1 < columns, 0 <= row2 < rows, 0 <= col2 < columns]:
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for r in range(len(matrix)):
        print(' '.join(map(str, matrix[r])))


