line_one = int(input())
line_two = int(input())

for char in range(line_one, line_two +1):
    ascii = chr(char)

    print(ascii, end = " ")