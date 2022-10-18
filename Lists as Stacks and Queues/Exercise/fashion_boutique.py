box_of_clothes = input().split()
rack_capacity = int(input())

racks = 0
current_sum = 0

while box_of_clothes:
    current_sum += int(box_of_clothes[-1])
    if current_sum <= rack_capacity:
        box_of_clothes.pop()
        if not box_of_clothes:
            racks += 1
        else:
            continue
    else:
        racks += 1
        current_sum = 0

print(racks)


