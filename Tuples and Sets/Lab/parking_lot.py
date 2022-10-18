count = int(input())
parking_lot = set()

for _ in range(count):
    inline = input().split(', ')
    direction = inline[0]
    plate = inline[1]

    if direction == "IN":
        if plate not in parking_lot:
            parking_lot.add(plate)
    elif direction == "OUT":
        if plate in parking_lot:
            parking_lot.remove(plate)

if not parking_lot:
    print("Parking Lot is Empty")
else:
    print('\n'.join(parking_lot))