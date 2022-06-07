letter_one = input()
letter_two = input()
letter_three = input()
number_one = ord(letter_one)
number_two = ord(letter_two)
number_three = ord(letter_three)
count = 0
for index_one in range(number_one, number_two +1):
    if index_one == number_three:
        continue
    for index_two in range(number_one, number_two + 1):
        if index_two == number_three:
            continue
        for index_three in range(number_one, number_two + 1):
            if index_three == number_three:
                continue
            count += 1
            print(f"{chr(index_one)}", end="")
            print(f"{chr(index_two)}", end="")
            print(f"{chr(index_three)}", end=" ")

print(count)