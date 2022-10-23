from collections import deque

bowls = deque([int(x) for x in input().split(", ")])
customers = deque([int(x) for x in input().split(", ")])

while customers and bowls:
    last_bowl = bowls.pop()
    first_customer = customers.popleft()
    if last_bowl == first_customer:
        continue
    elif last_bowl > first_customer:
        bowls.append(last_bowl - first_customer)
    elif last_bowl < first_customer:
        customers.appendleft(first_customer - last_bowl)


if len(customers) <= 0:
    print("Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
