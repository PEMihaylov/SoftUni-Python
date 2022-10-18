from collections import deque

N = int(input())
tank = deque()
kilometers = deque()
current_liters = 0
station = 0
total_km = sum(kilometers)

for _ in range(N):
    inline = list(map(int, input().split()))
    liters, km = inline[0], inline[1]
    tank.append(liters)
    kilometers.append(km)

for idx in range(N):
    if current_liters + tank[0] < kilometers[0]:
        x, y = tank.popleft(), kilometers.popleft()
        tank.append(x)
        kilometers.append(y)
        current_liters = 0
        station = idx + 1
    else:
        current_liters += tank[0] - kilometers[0]
        x, y = tank.popleft(), kilometers.popleft()
        tank.append(x)
        kilometers.append(y)

# sum =
print(station)



