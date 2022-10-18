symbols = ["-", ",", ".", "!", "?"]

with open("./text.txt", "r") as opened_file:
    my_text = opened_file.readlines()

for idx in range(0, len(my_text), 2):
    for symbol in symbols:
        my_text[idx] = my_text[idx].replace(symbol, "@")

    print(' '.join(my_text[idx].split()[::-1]))
