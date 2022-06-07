n = int(input())

musala = 0
monblan = 0
kilimandzharo = 0
k2 = 0
everest = 0
total_climbers = 0

for i in range(1, n +1):
    group_climbers = int(input())
    total_climbers += group_climbers
    if group_climbers <= 5:
        musala += group_climbers
    elif group_climbers <= 12:
        monblan += group_climbers
    elif group_climbers <= 25:
        kilimandzharo += group_climbers
    elif group_climbers <= 40:
        k2 += group_climbers
    elif group_climbers >= 41:
        everest += group_climbers

p1 = musala / total_climbers * 100
p2 = monblan / total_climbers * 100
p3 = kilimandzharo / total_climbers * 100
p4 = k2 / total_climbers * 100
p5 = everest / total_climbers * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
