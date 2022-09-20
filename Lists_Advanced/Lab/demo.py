# List comprehension
x = [num for num in range(5)]


# ver.1
num_list = list()

for i in range(1,7):
    if i % 2 == 0:
        num_list.append(i)

print(num_list)


# ver.2
num_list2 = [i for i in range(1,7) if i % 2 == 0]

print(num_list2)


# ver.1

num_list3 = list()

for i in range(1,7):
    if i % 2 == 0:
        num_list3.append(True)
    else:
        num_list3.append(False)

print(num_list3)

# ver.2

num_list2 = [True if i % 2 == 0 else False for i in range(1,7)]

print(num_list2)