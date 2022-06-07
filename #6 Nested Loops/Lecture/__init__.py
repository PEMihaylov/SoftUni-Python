letter_one = input()
letter_two = input()
letter_three = input()
number_one = ord(letter_one)
number_two = ord(letter_two)
number_three = ord(letter_three)

for index_one in range(number_one, number_two +1):
    for index_two in range(number_one, number_two + 1):
        for index_three in range(number_one, number_two + 1):
            print(f"{chr(index_one)}", end="")
            print(f"{index_two}", end="")
            print(f"{index_three}", end=" ")


