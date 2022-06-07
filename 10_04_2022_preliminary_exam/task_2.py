shirt = float(input())
budget = float(input())

shorts = shirt * 0.75
socks = shorts * 0.20
shoes = 2 * (shorts + shirt)

total_spend = (shorts + shirt + shoes + socks) * 0.85

diff = abs(total_spend - budget)

if total_spend >= budget:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_spend:.2f} lv.")
else:
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")
