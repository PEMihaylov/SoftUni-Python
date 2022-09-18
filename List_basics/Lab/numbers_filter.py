# number = int(input())
#
# numbers_list = list()
#
# for i in range(number):
#     current = int(input())
#     numbers_list.append(current)
#
# filtered_word = input()
# filtered = list()
#
# for current_number in numbers_list:
#     if filtered_word == "even":
#         if current_number % 2 == 0:
#             filtered.append(current_number)
#     if filtered_word == "odd":
#         if current_number % 2 != 0:
#             filtered.append(current_number)
#     if filtered_word == "positive":
#         if current_number >= 0:
#             filtered.append(current_number)
#     if filtered_word == "negative":
#         if current_number < 0:
#             filtered.append(current_number)
#
# print(filtered)



# number = int(input())
#
# positive = list()
# negative = list()
# odd = list()
# even = list()
#
# for i in range(number):
#     current = int(input())
#     if current % 2 == 0:
#         even.append(current)
#     else:
#         odd.append(current)
#     if current >= 0:
#         positive.append(current)
#     else:
#         negative.append(current)

filter_word = input()#

# if filtered_word == "even":
#     print(even)
# if filtered_word == "odd":
#     print(odd)
# if filtered_word == "positive":
#     print(positive)
# if filtered_word == "negative":
#     print(negative)
#


number = int(input())

positive = list()
negative = list()
odd = list()
even = list()

for i in range(number):
    current = int(input())
    if current % 2 == 0:
        even.append(current)
    else:
        odd.append(current)
    if current >= 0:
        positive.append(current)
    else:
        negative.append(current)

filter_word = input()

print(eval(filter_word))