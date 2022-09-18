collection_of_items = input().split('|')
budget = float(input())
train_ticket = 150
profit = 0
sold_items = 0
sold_items_list = []
for item in collection_of_items:
    new_items = item.split('->')
    item_type = new_items[0]
    item_price = float(new_items[1])
    if budget >= item_price:
        if item_type == "Clothes":
            if item_price <= 50.00:
                budget -= item_price
                sold_items += round(item_price * 1.40, 2)
                profit += item_price * 0.40
                new_price = round(item_price * 1.40, 2)
                sold_items_list.append(new_price)
        elif item_type == "Shoes":
            if item_price <= 35.00:
                budget -= item_price
                sold_items += round(item_price * 1.40, 2)
                profit += item_price * 0.40
                new_price = round(item_price * 1.40, 2)
                sold_items_list.append(new_price)
        elif item_type == "Accessories":
            if item_price <= 20.50:
                budget -= item_price
                sold_items += round(item_price * 1.40, 2)
                profit += item_price * 0.40
                new_price = round(item_price * 1.40, 2)
                sold_items_list.append(new_price)

new_budget = budget + sold_items
print(' '.join(str(num) for num in sold_items_list))
print(f"Profit: {profit:.2f}")

if new_budget >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")