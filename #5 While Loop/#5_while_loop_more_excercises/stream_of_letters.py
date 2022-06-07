count_n = 0
count_o = 0
count_c = 0
letter = str(input())
first_time = True
first_pass = True
while letter != "End":
    while count_c < 2 and count_n < 2 and count_o < 2:

        if letter == "n":
            count_n += 1
            if count_n <= 1:
                first_time = True
            else:
                print(letter, end="")
        elif letter == "o":
            count_o += 1
            if count_o <= 1:
                first_time = True
            else:
                print(letter, end="")
        elif letter == "c":
            count_c += 1
            if count_c <= 1:
                first_time = True
            else:
                print(letter, end="")
        elif letter != "c" or letter != "c" or letter != "c":
            print(letter, end="")

        letter = str(input())