lines = int(input())
capacity = 0
for pouring in range(lines):
    liters = int(input())
    if liters > 255 - capacity:
        print("Insufficient capacity!")
        continue
    else:
        capacity += liters

print(capacity)
