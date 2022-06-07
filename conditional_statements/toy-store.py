trip_price = float(input())
puzzle_count = int(input())
dolls_count = int(input())
teddy_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzle_price = puzzle_count * 2.60
dolls_price = dolls_count * 3
teddy_price = teddy_count * 4.10
minions_price = minions_count * 8.20
trucks_price = trucks_count * 2

total_price = puzzle_price + dolls_price + teddy_price + minions_price + trucks_price

total_count = puzzle_count + dolls_count + teddy_count + minions_count + trucks_count

if total_count >= 50:
    total_price = total_price * 0.75

total_price = total_price * 0.90

diff = abs(trip_price - total_price)
if trip_price <= total_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")