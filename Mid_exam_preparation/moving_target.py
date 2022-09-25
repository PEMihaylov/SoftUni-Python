targets = input().split(" ")
targets = list(map(int, targets))

command_line = input()

while command_line != "End":
    command_list = command_line.split(" ")
    command = command_list[0]
    index = int(command_list[1])
    value = int(command_list[2])

    if command == "Shoot" and index >= 0 and index < len(targets):
        current_target = targets[index]
        current_target -= value
        if current_target <= 0:
            targets.pop(index)
        else:
            targets[index] = current_target

    elif command == "Add":
        if index >= 0 and index < len(targets):
            targets.insert(index,value)
        else:
            print("Invalid placement!")

    elif command == "Strike":
        if index - value >= 0 and index + value < len(targets):
            targets = targets[0:index - value] + targets[index + value + 1:]
        else:
            print("Strike missed")
    command_line = input()

targets = list(map(str, targets))
output = "|".join(targets)
print(output)



#...mine......

targets = list(map(int, input().split()))
text = input()
while text != "End":
    data = text.split()
    command = data[0]
    index = int(data[1])
    value = int(data[2])
    if 0 <= index < len(targets):
        if command == "Shoot":
            targets[index] -= value
            if targets[index] <= 0:
                del targets[index]
        elif command == "Add":
            targets.insert(index, value)
        elif command == "Strike":
            if index - value < 0 or index - value > len(targets):
                print("Strike missed!")
            else:
                targets = targets[:index - value] + targets[index+value+1:]
    else:
        if command == "Add":
            print("Invalid placement!")

    text = input()

print('|'.join(str(x) for x in targets))

