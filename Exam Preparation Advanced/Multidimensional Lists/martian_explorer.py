matrix = [[x for x in input().split()]for k in range(6)]
rover = []
for r in range(6):
    if "E" in matrix[r]:
        rover = [r, matrix[r].index("E")]
water_deposit = 0
metal_deposit = 0
concrete_deposit = 0
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

commands = input().split(", ")
for command in commands:
    row = directions[command][0] + rover[0]
    col = directions[command][1] + rover[1]
    if row == -1:
        row = 5
    if row == 6:
        row = 0
    if col == -1:
        col = 5
    if col == 6:
        col = 0
    rover = [row, col]
    if matrix[row][col] == "W":
        water_deposit += 1
        print(f"Water deposit found at ({row}, {col})")
    elif matrix[row][col] == "M":
        metal_deposit += 1
        print(f"Metal deposit found at ({row}, {col})")
    elif matrix[row][col] == "C":
        concrete_deposit += 1
        print(f"Concrete deposit found at ({row}, {col})")
    elif matrix[row][col] == "R":
        print(f"Rover got broken at ({row}, {col})")
        break

if metal_deposit and water_deposit and concrete_deposit:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
