first_string = input()
second_string = input()
final_string = ''
for index in range(len(first_string)):
    final_string = second_string[:index + 1:] + first_string[index + 1::]
    if first_string[index] != second_string[index]:
        print(final_string)
