numbers = input().split(" ")
numbers = list(map(int, numbers))
command_line = input()

while command_line != "end":
    if command_line == "decrease":
        numbers = list(map(lambda n: n-1, numbers))
    else:
        explode = command_line.split(" ")
        command = explode[0]
        index1 = int(explode[1])
        index2 = int(explode[2])

        if command == "swap":
            numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
        elif command == "multiply":
            numbers[index1] = numbers[index1] * numbers[index2]

    command_line = input()

numbers = list(map(str, numbers))
output = ", ".join(numbers)
print(output)


#..........................
data = list(map(int, input().split()))
new_array = []
inline = input()
while inline != "end":
    if inline == "decrease":
        data = list([x-1 for x in data])
    else:
        text = inline.split()
        command = text[0]
        index_one = int(text[1])
        index_two = int(text[2])
        if command == "swap":
            data[index_one], data[index_two] = data[index_two], data[index_one]
        elif command == "multiply":
            data[index_one] = data[index_one] * data[index_two]

    inline = input()

print(', '.join(str(x) for x in data))