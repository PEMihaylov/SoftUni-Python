matrix = [[x for x in input().split()] for i in range(5)]
count = int(input())
target_count = 0
targets_pos = []
my_position = []

shots = 0
for w in range(5):
    for t in range(5):
        if matrix[w][t] == "x":
            shots += 1

for r in range(5):
    for l in range(5):
        if matrix[r][l] == "A":
            my_position = [r, l]
            matrix[r][l] = "."
my_row, my_col = my_position[0], my_position[1]

all_targets = shots
for num in range(count):
    if all_targets == 0:
        break
    command = input().split()
    if command[0] == "shoot":
        if command[1] == "up":
            for n in range(1, 5):
                if not 0 <= my_row - n < 5:
                    break
                if matrix[my_row - n][my_col] == "x":
                    target_count += 1
                    all_targets -= 1
                    matrix[my_row - n][my_col] = "."
                    targets_pos.append([my_row - n, my_col])
                    break
        elif command[1] == "down":
            for n in range(1, 5):
                if not 0 <= my_row + n < 5:
                    break
                if matrix[my_row + n][my_col] == "x":
                    target_count += 1
                    all_targets -= 1
                    matrix[my_row + n][my_col] = "."
                    targets_pos.append([my_row + n, my_col])
                    break
        elif command[1] == "left":
            for n in range(1, 5):
                if not 0 <= my_col - n < 5:
                    break
                if matrix[my_row][my_col - n] == "x":
                    target_count += 1
                    all_targets -= 1
                    matrix[my_row][my_col - n] = "."
                    targets_pos.append([my_row, my_col - n])
                    break
        elif command[1] == "right":
            for n in range(1, 5):
                if not 0 <= my_col + n < 5:
                    break
                if matrix[my_row][my_col + n] == "x":
                    target_count += 1
                    all_targets -= 1
                    matrix[my_row][my_col + n] = "."
                    targets_pos.append([my_row, my_col + n])
                    break

    elif command[0] == "move":
        step = int(command[-1])
        if command[1] == "up":
            if not 0 <= my_row - step < 5:
                continue
            if matrix[my_row - step][my_col] == ".":
                my_row = my_row - step
        elif command[1] == "down":
            if not 0 <= my_row + step < 5:
                continue
            if matrix[my_row + step][my_col] == ".":
                my_row = my_row + step
        elif command[1] == "left":
            if not 0 <= my_col - step < 5:
                continue
            if matrix[my_row][my_col - step] == ".":
                my_col = my_col - step
        elif command[1] == "right":
            if not 0 <= my_col + step < 5:
                continue
            if matrix[my_row][my_col + step] == ".":
                my_col = my_col + step

targets_left = 0
for w in range(5):
    for t in range(5):
        if matrix[w][t] == "x":
            targets_left += 1

if targets_left > 0:
    print(f"Training not completed! {targets_left} targets left.")
else:
    print(f"Training completed! All {target_count} targets hit.")


