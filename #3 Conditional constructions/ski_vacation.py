days_of_stay = int(input())
type_of_room = input()
evaluation = input()

room_price = 0
if type_of_room == "room for one person":
    room_price = 18.00
elif type_of_room == "apartment":
    room_price = 25.00
    if days_of_stay < 10:
        room_price = room_price * 0.70
    elif days_of_stay >= 10 and days_of_stay <= 15:
        room_price = room_price * 0.65
    elif days_of_stay > 15:
        room_price = room_price * 0.50
elif type_of_room == "president apartment":
    room_price = 35.00
    if days_of_stay < 10:
        room_price = room_price * 0.90
    elif days_of_stay >= 10 and days_of_stay <= 15:
        room_price = room_price * 0.85
    elif days_of_stay > 15:
        room_price = room_price * 0.80

nights_per_stay = days_of_stay - 1
total_price = room_price * nights_per_stay

if evaluation == "positive":
    total_price = total_price * 1.25
elif evaluation == "negative":
    total_price = total_price * 0.90

print(f"{total_price:.2f}")