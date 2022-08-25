import math

num_of_comp = int(input())
days = int(input())
total_coins = 0
for curr_day in range(1, days + 1):
    if curr_day % 10 == 0:
        num_of_comp -= 2
    if curr_day % 15 == 0:
        num_of_comp += 5
    total_coins += 50
    total_coins -= 2 * num_of_comp
    if curr_day % 3 == 0:
        total_coins -= 3 * num_of_comp
        if curr_day % 5 == 0:
            total_coins -= 2 * num_of_comp
    if curr_day % 5 == 0:
        total_coins += 20 * num_of_comp
        # if curr_day % 3 == 0:
        #     total_coins -= 2 * num_of_comp

coins_per_comp = math.floor(int(total_coins / num_of_comp))
print(f"{num_of_comp} companions received {coins_per_comp} coins each.")
