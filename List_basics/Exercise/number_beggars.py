sums_list = input().split(", ")
count_of_beggars = int(input())
final_list = []
counter_of_index = 0
sums_list_as_digits = []
# sums_list_as_digits = [int(i) for i in sums_list]
for string in sums_list:
    sums_list_as_digits.append(int(string))

while counter_of_index < count_of_beggars:
    sum_for_current_beggar = 0
    for currrent_index in range(counter_of_index, len(sums_list_as_digits), count_of_beggars):
        sum_for_current_beggar += sums_list_as_digits[currrent_index]
    counter_of_index += 1
    final_list.append((sum_for_current_beggar))


print(final_list)



#
# collect_list = list(map(int, input().split(", ")))
#
# collectors = int(input())
#
# collector_final = []
#
# for i in range(collectors):
#     middle_list = collect_list[i::collectors]
#     collector_final.append(sum(middle_list))
#
# print(collector_final)