# list = [2,3,4,5,6,-8]
# min_number = min(list)
# list.remove(min_number)
# print(list)
# # print(max(list))


# list_of_numbers = list(map(int, input().split()))
# remove_count = int(input())
#
# for j in range(remove_count):
#     min_number = min(list_of_numbers)
#     for i in list_of_numbers:
#         if i == min_number:
#             list_of_numbers.remove(min_number)
#
# final_list = ', '.join(str(x) for x in list_of_numbers)
#
# print(final_list)



list_of_numbers = list(map(int, input().split()))
remove_count = int(input())

for j in range(remove_count):
    min_number = min(list_of_numbers)
    list_of_numbers.remove(min_number)

final_list = ', '.join(str(x) for x in list_of_numbers)

print(final_list)


new_list = input().split()
count = int(input())

new_list = [int(x) for x in new_list]
# new_list.sort()

for rem in range(count):
    new_list.remove(min(new_list))

new_list = [str(x) for x in new_list]
print(', '.join(new_list))