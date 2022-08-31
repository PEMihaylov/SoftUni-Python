# first_string, second_string = input().split()
# Equal to
# some_string = input().split()
# first_string = some_string[0]
# second_string = some_string[1]

first_string, second_string = input().split()
total_sum = 0
if len(first_string) > len(second_string):
    for index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[index])
elif len(second_string) > len(first_string):
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[index])
elif len(first_string) == len(second_string):  # else
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
print(total_sum)

#................................

text = input().split()
str1 = text[0]
str2 = text[1]

total_sum = 0

if len(str1) < len(str2):
    for index in range(len(str1), len(str2)):
        total_sum += ord(str2[index])
    for index in range(len(str1)):
        total_sum += ord(str1[index]) * ord(str2[index])

elif len(str1) > len(str2):
    for index in range(len(str2), len(str1)):
        total_sum += ord(str1[index])
    for index in range(len(str2)):
        total_sum += ord(str1[index]) * ord(str2[index])

elif len(str1) == len(str2):
    for index in range(len(str1)):
        total_sum += ord(str1[index]) * ord(str2[index])

print(total_sum)