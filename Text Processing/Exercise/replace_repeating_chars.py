text = input()
new_string = " "

for ch in text:
    if new_string[-1] == ch:
        continue
    new_string += ch

print(new_string[1:])