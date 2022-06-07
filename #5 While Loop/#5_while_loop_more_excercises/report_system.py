gathered_sum = int(input())
donation_counter = 0
cash_transaction = 0
cash_count = 0
card_transaction = 0
card_count = 0

price_of_things = input()
while price_of_things != "End":
    current_price = int(price_of_things)
    donation_counter += 1
    if donation_counter % 2 != 0 and current_price <= 100:
        gathered_sum -= current_price
        cash_transaction += current_price
        cash_count += 1
        print("Product sold!")
    elif donation_counter % 2 != 0 and current_price > 100:
        print("Error in transaction!")
    elif donation_counter % 2 == 0 and current_price >= 10:
        gathered_sum -= current_price
        card_transaction += current_price
        card_count += 1
        print("Product sold!")
    elif donation_counter % 2 == 0 and current_price < 10:
        print("Error in transaction!")

    if gathered_sum <= 0:
        break
    price_of_things = input()

if gathered_sum <= 0:
    avg_cash_transaction = cash_transaction / cash_count
    print(f"Average CS: {avg_cash_transaction:.2f}")
    avg_card_transaction = card_transaction / card_count
    print(f"Average CC: {avg_card_transaction:.2f}")
else:
    print("Failed to collect required money for charity.")
