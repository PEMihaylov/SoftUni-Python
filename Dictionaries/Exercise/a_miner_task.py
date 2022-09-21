resources = {}

while True:
    current_resource = input()
    if current_resource == "stop":
        break
    quantity = int(input())
    if current_resource not in resources.keys():
        resources[current_resource] = 0
    resources[current_resource] += quantity

for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")




# #...mine..........
# strings = input()
# resources = {}
# while strings != "stop":
#     str_count = int(input())
#
#     if strings not in resources.keys():
#         resources[strings] = 0
#     resources[strings] += str_count
#
#     strings = input()
#
# for resource, quantity in resources.items():
#     print(f"{resource} -> {quantity}")