names = input().split(", ")
matrix = [[x for x in input().split()] for i in range(6)]
rest_list = []
while True:
    coordinates = input()
    row = int(coordinates[1])
    col = int(coordinates[4])
    if names[0] in rest_list:
        rest_list.remove(names[0])
        names[0], names[1] = names[1], names[0]
        continue

    if matrix[row][col] == "E":
        print(f"{names[0]} found the Exit and wins the game!")
        break
    elif matrix[row][col] == "T":
        print(f"{names[0]} is out of the game! The winner is {names[1]}.")
        break
    elif matrix[row][col] == "W":
        print(f"{names[0]} hits a wall and needs to rest.")
        rest_list.append(names[0])
        names[0], names[1] = names[1], names[0]
        continue
    else:
        names[0], names[1] = names[1], names[0]

