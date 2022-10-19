rows = int(input())

matrix = [[int(x) for x in input().split()] for i in range(rows)]

while True:
    entry = input()
    if entry == "END":
        break

    command = entry.split()

    row, col, value = int(command[1]), int(command[2]), int(command[3])

    if row < 0 or row >= rows or col < 0 or col >= rows:
        print("Invalid coordinates")

    elif command[0] == "Add":
        matrix[row][col] += value

    elif command[0] == "Subtract":
        matrix[row][col] -= value


[print(*row) for row in matrix]
# for n in range(rows):
#     print(' '.join(map(str, matrix[n])))
