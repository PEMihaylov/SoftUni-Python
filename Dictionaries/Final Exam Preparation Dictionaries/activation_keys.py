key = input()

while True:
    command = input().split(">>>")
    current_command = command[0]

    if current_command == "Generate":
        print(f"Your activation key is: {key}")
        break

    elif current_command == "Slice":
        key = key[:(command[1])] + key[int(command[2]):]
        print(key)

    elif current_command == "Flip":
        if command[1] == "Upper":
            key = key[:int(command[2])] + key[int(command[2]):int(command[3])].upper() + key[int(command[3]):]
        else:
            key = key[:int(command[2])] + key[int(command[2]):int(command[3])].lower() + key[int(command[3]):]

            print(key)

    elif current_command == "Contains":
        substring = command[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print("Substring not found!")

#....Moeto.......

activ_key = input()
string = input()
while string != "Generate":
    data = string.split(">>>")
    command = data[0]
    if command == "Contains":
        substring = data[1]
        if substring in activ_key:
            print(f"{activ_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command == "Flip":
        case = data[1]
        start_index = int(data[2])
        end_index = int(data[3])
        if case == "Upper":
            activ_key = activ_key[:start_index] + activ_key[start_index:end_index].upper() + activ_key[end_index:]
            print(activ_key)
        elif case == "Lower":
            activ_key = activ_key[:start_index] + activ_key[start_index:end_index].lower() + activ_key[end_index:]
            print(activ_key)

    elif command == "Slice":
        start_index = int(data[1])
        end_index = int(data[2])
        activ_key = activ_key[:start_index] + activ_key[end_index:]
        print(activ_key)


    string = input()

print(f"Your activation key is: {activ_key}")



# key = input()

key = input()

while True:
    command = input().split('>>>')
    current_command = command[0]

    if current_command == 'Generate':
        print(f"Your activation key is: {key}")
        break

    elif current_command == 'Slice':
        key = key[:int(command[1])] + key[int(command[2]):]
        print(key)

    elif current_command == 'Flip':
        if command[1] == 'Upper':
            key = key[:int(command[2])] + key[int(command[2]):int(command[3])].upper() + key[int(command[3]):]
        else:
            key = key[:int(command[2])] + key[int(command[2]):int(command[3])].lower() + key[int(command[3]):]

        print(key)

    elif current_command == 'Contains':
        substring = command[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print(f"Substring not found!")

