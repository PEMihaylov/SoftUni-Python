concealed_msg = input()
inline = input()
while inline != "Reveal":
    data = inline.split(":|:")
    command = data[0]
    if command == "InsertSpace":
        index = int(data[1])
        concealed_msg = concealed_msg[:index] + " " + concealed_msg[index:]
        print(concealed_msg)
    elif command == "Reverse":
        substring = data[1]
        if substring in concealed_msg:
            substring_rev = substring[::-1]
            sub_index = concealed_msg.index(substring)
            concealed_msg = concealed_msg[:sub_index] + concealed_msg[sub_index + len(substring):]
            concealed_msg += substring_rev
            print(concealed_msg)
        else:
            print("error")
    elif command == "ChangeAll":
        substring_all = data[1]
        replacement = data[2]
        concealed_msg = concealed_msg.replace(substring_all, replacement)
        print(concealed_msg)

    inline = input()

print(f"You have a new text message: {concealed_msg}")
