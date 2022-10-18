from collections import deque
queue = deque()
liters = int(input())
name = input()
while name != "Start":
    queue.append(name)
    name = input()

command = input()
while command != "End":
    if "refill" in command:
        data = command.split()
        add_liters = int(data[1])
        liters += add_liters
    else:
        new_liters = int(command)
        if new_liters <= liters:
            liters -= new_liters
            print(f"{queue.popleft()} got water" )
        else:
            print(f"{queue.popleft()} must wait" )

    command = input()

print(f"{liters} liters left")



#...lectures solution

# from collections import deque
# queue = deque()
# water_quantity = int(input())
# name = input()
# # add people to queue
# command = input()
# while command != "End":
#     if "refill" in command:
#         # increase liters
#     else:
#         liters = int(command)
#         if liters <= water_quantity:
#             water_quantity -= liters
#             print(f"{queue.popleft()} got water")
#         else:
#             print(f'{queue.popleft()} must wait')
#     command = input()
# print(f"{water_quantity} liters left")
