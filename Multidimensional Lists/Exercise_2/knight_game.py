N = int(input())
matrix = [list(input()) for k in range(N)]
positions = (
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2),
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
)

removed_knights = 0

while True:
    max_attacks = 0
    best_knight = []
    for row in range(N):
        for col in range(N):
            if matrix[row][col] == "K":
                attacks = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < N and 0 <= pos_col < N:
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    max_attacks = attacks
                    best_knight = [row, col]

    if best_knight:
        matrix[best_knight[0]][best_knight[1]] = "O"
        removed_knights += 1
    else:
        break

print(removed_knights)
