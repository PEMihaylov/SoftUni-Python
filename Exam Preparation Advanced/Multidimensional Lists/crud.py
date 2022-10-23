matrix = [[i for i in input().split()] for x in range(6)]
position = input()
row_i = int(position[1])
col_i = int(position[4])

directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

init_pos = [row_i, col_i]

inline = input()

while inline != "Stop":
    command = inline.split(', ')
    row, col = directions[command[1]][0] + init_pos[0], directions[command[1]][1] + init_pos[1]
    pos = matrix[row][col]

    if command[0] == "Create":
        if not pos.isalnum():
            matrix[row][col] = command[-1]
    elif command[0] == "Update":
        if pos.isalnum():
            matrix[row][col] = command[-1]
    elif command[0] == "Delete":
        if pos.isalnum():
            matrix[row][col] = "."
    elif command[0] == "Read":
        if pos.isalnum():
            print(matrix[row][col])
    init_pos = [row, col]


    inline = input()

[print(*rows) for rows in matrix]