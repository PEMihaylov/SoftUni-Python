def merge_func(start_index, end_index, message):
    return message[start_index] + message[end_index]


def divide_func(index, partitions, message):
    return message[index][0:2]


message = input().split()
string = input()
while string != "3:1":
    data = string.split()
    command = data[0]
    if command == "merge":
        start_index = int(data[1])
        end_index = int(data[2])
        if start_index < len(message) and end_index < len(message):
            merge_func(start_index, end_index, message)
    elif command == "divide":
        index = int(data[1])
        partitions = int(data[2])
        divide_func(index, partitions, message)

    string = input()