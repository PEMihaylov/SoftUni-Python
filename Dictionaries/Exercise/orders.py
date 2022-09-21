data = input()
orders_book = {}
while True:
    if data == "buy":
        break

    command = data.split()
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if product not in orders_book.keys():
        orders_book[product] = [price, quantity]

    elif product in orders_book.keys():
        orders_book[product] = [price, (quantity + orders_book[product][1])]

    data = input()

for key, value in orders_book.items():
    total = orders_book[key][0] * orders_book[key][1]
    print(f"{key} -> {total:.2f}")
