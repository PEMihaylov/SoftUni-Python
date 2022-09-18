factor_number = int(input())
count_number = int(input())

new_list = []
for element in range(1, count_number+1):
    new_list.append(element*factor_number)


print(new_list)