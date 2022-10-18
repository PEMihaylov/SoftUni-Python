import os

command_line = input()

while command_line != "End":
    command_line = command_line.split("-")
    command = command_line[0]
    file_name = command_line[1]

    if command == "Create":
        file = open(file_name, "w")
        file.close()

    elif command == "Add":
        text = command_line[2]
        with open(file_name, "a") as file:
            file.write(f"{text}\n")

    elif command == "Replace":
        try:
            file = open(file_name, "r+")
            old_string = command_line[2]
            replacement = command_line[3]
            lines = file.readlines()
            for idx in range(len(lines)):
                lines[idx] = lines[idx].replace(old_string, replacement)
            file = open(file_name, "w")
            file.write(''.join(lines))
            file.close()
        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")

    command_line = input()