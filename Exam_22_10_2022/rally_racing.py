size = int(input())
racing_number = input()
track = [[x for x in input().split()] for i in range(size)]
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
total_km = 0
tunnel_1 = []
tunnel_2 = []
is_finished = False
for r in range(size):
    if "T" in track[r]:
        tunnel_1 = [r, track[r].index("T")]
        track[r][track[r].index("T")] = "T1"
        break

for j in range(size):
    if "T" in track[j]:
        tunnel_2 = [j, track[j].index("T")]

row_i, col_i = [0, 0]
command = input()
while command != "End":
    row = directions[command][0] + row_i
    col = directions[command][1] + col_i

    if track[row][col] == ".":
        total_km += 10
        row_i, col_i = row, col

    elif track[row][col] == "T":
        total_km += 30
        track[row][col] = "."
        row_i, col_i = tunnel_1[0], tunnel_1[1]
        track[row_i][col_i] = "."

    elif track[row][col] == "T1":
        total_km += 30
        track[row][col] = "."
        row_i, col_i = tunnel_2[0], tunnel_2[1]
        track[row_i][col_i] = "."

    elif track[row][col] == "F":
        total_km += 10
        is_finished = True
        break

    command = input()

track[row][col] = "C"

for r in range(size):
    if "T1" in track[r]:
        track[r][track[r].index("T1")] = "T"
        break

if is_finished:
    print(f"Racing car {racing_number} finished the stage!")
else:
    print(f"Racing car {racing_number} DNF.")

print(f"Distance covered {total_km} km.")

for n in range(size):
    print(''.join(map(str, track[n])))
