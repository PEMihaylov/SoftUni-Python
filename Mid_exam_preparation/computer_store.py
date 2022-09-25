new_receipt = input()
total_price = 0

while new_receipt != "special" and new_receipt != "regular":
    current_price = float(new_receipt)
    if current_price > 0:
        total_price += current_price

    else:
        print("Invalid price!")
    new_receipt = input()

total_price_with_taxes = total_price * 1.2
total_amount_of_taxes = total_price * 0.2

if new_receipt == "special":
    total_price_with_taxes *= 0.9

if total_price <= 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!"
          f"\nPrice without taxes: {total_price:.2f}$\n"
          f"Taxes: {total_amount_of_taxes:.2f}$\n"
          "-----------\n"
          f"Total price: {total_price_with_taxes:.2f}$"
          )



#..........moeto

part_price = input()
total_price = 0
while part_price != "special" and part_price != "regular":
    if float(part_price) < 0:
        print("Invalid price!")
    else:
        total_price += float(part_price)

    part_price = input()

total_price_taxes = total_price * 1.2

if part_price == "special":
    total_price_taxes = total_price_taxes * 0.9

if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {(total_price * 0.2):.2f}$")
    print("-----------")
    print(f"Total price: {total_price_taxes:.2f}$")