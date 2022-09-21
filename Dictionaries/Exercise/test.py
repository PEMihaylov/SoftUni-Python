# def merge_func(start_index, end_index, message):
#     return message[start_index] + message[end_index]


# def divide_func(index, partitions, message):
#     return message[index].split(" ", partitions)
#
# message_test = input().split()
# data = input().split()
# # start_index = int(data[0])
# # end_index = int(data[1])
#
# index = int(data[0])
# partitions = int(data[1])
#
# # print(merge_func(start_index, end_index, message_test))
# print(divide_func(index, partitions, message_test))

#
# my_list = ["asdacd", "ghi", "jkl"]
# my_list = list(map(lambda x: x.replace(name, "Blacklisted")))
# result = my_list[0][0:1]
# news = my_list[0].replace(result, "*")
#
# print(result)
# print(news)

# Replace Values in a List using Lambda Function

# define list
l = ['Hardik', 'Rohit', 'Rahul', 'Virat', 'Pant']

# replace Pant with Ishan
l = list(map(lambda x: x.replace('Pant', 'Ishan'), l))

# print list
print(l)