from collections import deque

qty = int(input())

orders = deque(map(int, input().split()))

print(max(orders))

while orders:
    if orders[0] <= qty:
        qty -= orders[0]
        orders.popleft()
    else:
        break

if not orders:
    print("Orders complete")

else:
    # print("Orders left: ", end="")
    # print(*orders)
    print("Orders left:", *orders, sep=" ")