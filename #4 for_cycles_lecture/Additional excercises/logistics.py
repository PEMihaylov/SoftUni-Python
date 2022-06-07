load_number = int(input())
price_of_load = 0
bus_count = 0
camion_count = 0
train_count = 0
total_price = 0
total_weight = 0
for load in range(1, load_number + 1):
    load_weight = int(input())
    if load_weight <= 3:
        total_price += (load_weight * 200)
        bus_count += load_weight
        total_weight += load_weight

    elif load_weight <= 11:
        total_price += (load_weight * 175)
        camion_count += load_weight
        total_weight += load_weight

    else:
        total_price += (load_weight * 120)
        train_count += load_weight
        total_weight += load_weight

avg_price = total_price / total_weight
print(f"{avg_price:.2f}")

bus_percent = bus_count / total_weight * 100
print(f"{bus_percent:.2f}%")

camion_percent = camion_count / total_weight * 100
print(f"{camion_percent:.2f}%")

train_percent = train_count / total_weight * 100
print(f"{train_percent:.2f}%")