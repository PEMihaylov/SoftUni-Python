gifts = input().split()
command_line = input()
while command_line != "No Money":
    deciphered_line = command_line.split()
    if len(deciphered_line) == 3:
        command = deciphered_line[0]
        gift = deciphered_line[1]
        index = int(deciphered_line[2])
        if command == "Required":
            if 0 < int(index) < len(gifts):
                gifts[index] = gift

    elif len(deciphered_line) == 2:
        command = deciphered_line[0]
        gift = deciphered_line[1]

        if command == "OutOfStock":
            for i in range(len(gifts)):
                if gifts[i] == gift:
                    gifts[i] = "None"

        elif command == "JustInCase":
            gifts[-1] = gift

    command_line = input()

final_list = []
for i in gifts:
    if i not in final_list:
        final_list.append(i)

if "None" in final_list:
    final_list.remove("None")
#
print(' '.join(final_list))
