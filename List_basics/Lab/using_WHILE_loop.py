# my_list = ["dog", "cat", "fish"]
# i = 0
# while i < len(my_list):
#     print(my_list[i], end=" ")
#     i += 1


my_list = ["dog", "cat", "fish"]

while my_list:
    print(my_list[0], end=" ")
    current_element = my_list[0]
    my_list.remove(current_element)
 