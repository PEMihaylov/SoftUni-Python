size = int(input())
matrix = [[x for x in input().split()] for _ in range(size)]
direction = [0, 0, 0, 0]
bunny = []
best_direction = ""
best_positions = []


for row in range(size):
    for col in range(size):
        if matrix[row][col] == "B":
            bunny = [row, col]
row_x, col_x = bunny[0], bunny[1]

curr_pos = []
for pos in range(1, size):
    if row_x - pos >= 0:
        if matrix[row_x - pos][col_x] == "X":
            break

        else:
            direction[2] += int(matrix[row_x - pos][col_x])
            curr_pos.append([row_x - pos, col_x])
            if direction[2] == max(direction):
                best_direction = "up"
                best_positions = curr_pos

    else:
        break

curr_pos = []
for pos in range(1, size):
    if row_x + pos < len(matrix):
        if matrix[row_x + pos][col_x] == "X":
            break
        else:
            direction[3] += int(matrix[row_x + pos][col_x])
            curr_pos.append([row_x + pos, col_x])
            if direction[3] == max(direction):
                best_direction = "down"
                best_positions = curr_pos
    else:
        break

curr_pos = []
for pos in range(1, size):
    if col_x - pos >= 0:
        if matrix[row_x][col_x - pos] == "X":
            break
        else:
            direction[0] += int(matrix[row_x][col_x - pos])
            curr_pos.append([row_x, col_x - pos])
            if direction[0] == max(direction):
                best_direction = "left"
                best_positions = curr_pos
    else:
        break

curr_pos = []
for pos in range(1, size):
    if col_x + pos < len(matrix):
        if matrix[row_x][col_x + pos] == "X":
            break
        else:
            direction[1] += int(matrix[row_x][col_x + pos])
            curr_pos.append([row_x, col_x + pos])
            if direction[1] == max(direction):
                best_direction = "right"
                best_positions = curr_pos

    else:
        break

print(best_direction)
print('\n'.join(map(str, best_positions)))
print(max(direction))
