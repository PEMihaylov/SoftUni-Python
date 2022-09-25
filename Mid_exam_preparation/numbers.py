def sorted_func(greater_numbers_than_average_sum):
    top_five_numbers = []

    for num in sorted(greater_numbers_than_average_sum)[::-1]:
        if len(top_five_numbers) < 5:
            top_five_numbers.append(num)
        else:
            break

    return ' '.join([str(num) for num in top_five_numbers])


def numbers_func(numbers):
    average_sum = sum(numbers) / len(numbers)
    greater_numbers_than_average_sum = [num for num in numbers if num > average_sum]
    if greater_numbers_than_average_sum:
        print(sorted_func(greater_numbers_than_average_sum))
    else:
        print('No')

nums = list(map(int, input().split(' ')))
numbers_func(nums)

#... moeto

# numbers = list(map(int, input().split()))
# total_sum = sum(numbers)
# avg = total_sum / len(numbers)
#
# new_list = []
#
# for num in numbers:
#     if num > avg:
#         new_list.append(num)
#
# new_list.sort()
# new_list = new_list[::-1]
# new_list = new_list[0:5]
# if new_list:
#     print(' '.join(str(x) for x in new_list))
# else:
#     print("No")