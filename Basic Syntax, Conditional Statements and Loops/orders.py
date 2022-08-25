number_of_orders = int(input())

total_price = 0

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsule_needed_per_day = int(input())
    if 0.01 <= price_per_capsule <= 100.00 and 1 <= days <= 31 and 1 <= capsule_needed_per_day <= 2000:
        current_order = days * price_per_capsule * capsule_needed_per_day
        total_price += current_order
    else:
        continue

    print(f"The price for the coffee is: ${current_order:.2f}")

print(f"Total: ${total_price:.2f}")
