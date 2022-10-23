desk = [[i for i in input().split()] for k in range(8)]
white_pos = []
black_pos = []

desk[0][0] = "a8"
columns = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
rows = {0: "8", 1: "7", 2: "6", 3: "5", 4: "4", 5: "3", 6: "2", 7: "1"}

cols = ""
for row in range(8):
    if "b" in desk[row]:
        black_pos = [row, desk[row].index("b")]
    if "w" in desk[row]:
        white_pos = [row, desk[row].index("w")]
positions = {"w": white_pos, "b": black_pos}

black_row, black_col = black_pos[0], black_pos[1]
white_row, white_col = white_pos[0], white_pos[1]
for turn in range(1, 8):

    white_row = white_pos[0] - 1
    if white_row == 0:
        print(f"Game over! White pawn is promoted to a queen at {columns[white_col] + rows[white_row]}.")
        break

    if white_row == black_row and (white_col == black_col + 1 or white_col == black_col - 1):
        print(f"Game over! White win, capture on {columns[black_col] + rows[black_row]}.")
        break

    black_row = black_pos[0] + 1
    if black_row == 7:
        print(f"Game over! Black pawn is promoted to a queen at {columns[black_col] + rows[black_row]}.")
        break

    if white_row == black_row and (black_col == white_col + 1 or black_col == white_col - 1):
        print(f"Game over! Black win, capture on {columns[white_col] + rows[white_row]}.")
        break

    white_pos[0] = white_pos[0] - 1
    black_pos[0] = black_pos[0] + 1

