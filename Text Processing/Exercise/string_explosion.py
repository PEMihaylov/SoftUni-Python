text = input()
new_string = ""
strenght = 0
for i in range(len(text)):
    if text[i] != ">" and strenght > 0:
        # new_string += text[i]
        strenght -= 1

    elif text[i] == ">":
        new_string += text[i]
        strenght += int(text[i + 1])

    else:
        new_string += text[i]

print(new_string)