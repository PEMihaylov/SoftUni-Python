def enough_materials(food, hay, cover):
    if food > 0 and hay >0 and cover > 0:
        return True
    else:
        return False

food_qty = float(input())
hay_qty = float(input())
cover_qty = float(input())
weight = float(input())
food_qty *= 1000
hay_qty *= 1000
cover_qty *= 1000
weight *= 1000

for day in range(1, 31):
    if day % 1 == 0:
        food_qty -= 300
    if day % 2 == 0:
        hay_qty -= food_qty * 0.05
    if day % 3 == 0:
        cover_qty -= weight / 3

if enough_materials(food_qty, hay_qty, cover_qty):
    print(f"Everything is fine! Puppy is happy! Food: {food_qty / 1000:.2f}, Hay: {hay_qty / 1000 :.2f}, Cover: {cover_qty / 1000:.2f}.")
else:
    print("Merry must go to the pet store!")