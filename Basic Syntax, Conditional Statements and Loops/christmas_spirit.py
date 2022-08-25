decorations_qty = int(input())
days_to_christ = int(input())
budget = 0
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
spirit_points = 0

for current_day in range(1, days_to_christ + 1):
    if current_day % 11 == 0:
        decorations_qty += 2
    if current_day % 2 == 0:
        budget += ornament_set_price * decorations_qty
        spirit_points += 5
    if current_day % 3 == 0:
        budget += (tree_garland_price + tree_skirt_price) * decorations_qty
        spirit_points += 13
    if current_day % 5 == 0:
        budget += tree_lights_price * decorations_qty
        spirit_points += 17
        if current_day % 3 == 0:
            spirit_points += 30
    if current_day % 10 == 0:
        spirit_points -= 20
        budget += tree_skirt_price + tree_garland_price + tree_lights_price

if days_to_christ % 10 == 0:
    spirit_points -= 30


print(f"Total cost: {budget}")
print(f"Total spirit: {spirit_points}")