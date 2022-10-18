numbers_dictionary = {}

first_line = input()

while first_line != "Search":
    try:
        number = int(input())
        if number not in numbers_dictionary:
            numbers_dictionary[first_line] = 0
        numbers_dictionary[first_line] = number
    except ValueError:
        print("The variable number must be an integer")

    first_line = input()

second_line = input()
while second_line != "Remove":
    try:
        print(numbers_dictionary[second_line])
    except KeyError:
        print("Number does not exist in dictionary")
    second_line = input()

third_line = input()
while third_line != "End":
    try:
        del numbers_dictionary[third_line]
    except KeyError:
        print("Number does not exist in dictionary")

    third_line = input()

print(numbers_dictionary)
