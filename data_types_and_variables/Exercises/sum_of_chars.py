lines_numbers = int(input())
sum = 0
for line in range(lines_numbers):
    letter = input()
    ascii = ord(letter)
    sum += int(ascii)

print(f"The sum equals: {sum}")