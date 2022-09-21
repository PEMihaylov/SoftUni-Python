# useful_items = {"shards": 0, "fragments": 0, "motes": 0}
# useless_items = {}
# obtained = False
# command = input().split()
# while True:
#     for index in range(0, len(command), 2):
#         value = int(command[index])
#         key = command[index + 1].lower()
#         if key == "shards" or key == "fragments" or key == "motes": # if key in useless_items.keys()
#             useful_items[key] += value
#         else:
#             if key not in useless_items.keys(): # in useless_items
#                 useless_items[key] = 0
#             useless_items[key] += value
#         if useful_items["shards"] >= 250:
#             print("Shadowmourne obtained!")
#             useful_items["shards"] -= 250
#             obtained = True
#         elif useful_items["fragments"] >= 250:
#             print("Valanyr obtained!")
#             useful_items["shards"] -= 250
#             obtained = True
#         elif useful_items["motes"] >= 250:
#             print("Dragonwrath obtained!")
#             useful_items["motes"] -= 250
#             obtained = True
#         if obtained:
#             break
#     if obtained:
#         break
#     command = input().split()
#
# for material, quantity in useful_items.items():
#     print(f"{material}: {quantity}")
# for material, quantity in useless_items.items():
#     print(f"{material}: {quantity}")

#.......................

items = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False
command = input().split()
while not obtained:
    for index in range(0, len(command), 2):
        value = int(command[index])
        key = command[index + 1].lower()
        if key not in items.keys(): #in useless_items
                items[key] = 0
        items[key] += value
        if items["shards"] >= 250:
            print("Shadowmourne obtained!")
            items["shards"] -= 250
            obtained = True
        elif items["fragments"] >= 250:
            print("Valanyr obtained!")
            items["fragments"] -= 250
            obtained = True
        elif items["motes"] >= 250:
            print("Dragonwrath obtained!")
            items["motes"] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break
    command = input().split()
for material,quantity in items.items():
    print(f"{material}: {quantity}")