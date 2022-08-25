budget = float(input())
flour_price = float(input())
current_budget = budget
eggs_price = 0.75 * flour_price
milk_price = 1.25 * flour_price
price_for_one_loaf = eggs_price + flour_price + (0.25 * milk_price)
coloured_eggs_count = 0
loaf_of_bread_count = 0

for x in range(0, int(current_budget), 1):
    if current_budget >= price_for_one_loaf:
        current_budget -= price_for_one_loaf
        loaf_of_bread_count += 1
        coloured_eggs_count += 3
        if loaf_of_bread_count % 3 == 0:
            coloured_eggs_count -= loaf_of_bread_count - 2
    else:
        break

print(f"You made {loaf_of_bread_count} loaves of Easter bread! Now you have {coloured_eggs_count} eggs and {current_budget:.2f}BGN left.")
