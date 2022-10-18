import string

file = open("./text.txt", "r")
opened_file = file.readlines()
num = 0
for line in opened_file:
    num += 1
    alpha_num = 0
    punct_num = 0
    for letter in line:
        if letter.isalpha():
            alpha_num += 1
        elif letter in string.punctuation:
            punct_num += 1

    new_text = f"Line {num}: {line} ({alpha_num})({punct_num})\n"


    final_file = open("./recorded_text.txt", "a")
    final_file.write(new_text)
    final_file.close()