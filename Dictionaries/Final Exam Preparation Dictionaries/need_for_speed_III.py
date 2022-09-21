def store_cars_information(cars_dictionary, number):
    for _ in range(number):
        data = input().split('|')
        brand = data[0]
        mileage = int(data[1])
        fuel = int(data[2])

        cars_dictionary[brand] = [mileage, fuel]

    return cars_dictionary


def special_commands(cars_dictionary):
    while True:
        command = input()

        if command == 'Stop':
            break

        command = command.split(' : ')
        current_command = command[0]
        brand = command[1]

        if current_command == 'Drive':
            distance = int(command[2])
            fuel = int(command[3])
            available_fuel = cars_dictionary[brand][1]
            current_mileage = cars_dictionary[brand][0]

            if available_fuel < fuel:
                print("Not enough fuel to make that ride")
            else:
                cars_dictionary[brand][1] -= fuel
                cars_dictionary[brand][0] += distance
                print(f"{brand} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

            if cars_dictionary[brand][0] >= 100000:
                del cars_dictionary[brand]
                print(f"Time to sell the {brand}!")

        elif current_command == 'Refuel':
            fuel = int(command[2])
            available_fuel = cars_dictionary[brand][1]

            if fuel + available_fuel > 75:
                fuel = 75 - available_fuel

            cars_dictionary[brand][1] += fuel

            print(f"{brand} refueled with {fuel} liters")

        elif current_command == 'Revert':
            kilometers = int(command[2])
            current_mileage = cars_dictionary[brand][0]

            if current_mileage - kilometers < 10000:
                cars_dictionary[brand][0] = 10000
            else:
                cars_dictionary[brand][0] -= kilometers
                print(f"{brand} mileage decreased by {kilometers} kilometers")

    return cars_dictionary


def additional_print_function(cars_dictionary):
    for brand in cars_dictionary:
        mileage = cars_dictionary[brand][0]
        fuel = cars_dictionary[brand][1]

        print(f'{brand} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.')


def need_for_speed(number):
    # The current dictionary contains a list with two values
    # At index 0 we have mileage, and at index 1 we have fuel
    cars_dictionary = {}

    store_cars_information(cars_dictionary, number)
    special_commands(cars_dictionary)
    additional_print_function(cars_dictionary)


n = int(input())
need_for_speed(n)


...#..moeto reshenie...
num = int(input())
nfs_book = {}
for n in range(num):
    inline = input().split('|')
    auto = inline[0]
    mileage = int(inline[1])
    fuel = int(inline[2])
    nfs_book[auto] = {'miles': mileage, 'brent': fuel}

text = input()
while text != "Stop":
    data = text.split(' : ')
    command = data[0]
    car = data[1]
    if command == "Drive":
        distance = int(data[2])
        oil = int(data[3])
        if nfs_book[car]['brent'] < oil:
            print("Not enough fuel to make that ride")
        else:
            nfs_book[car]['brent'] -= oil
            nfs_book[car]['miles'] += distance
            print(f"{car} driven for {distance} kilometers. {oil} liters of fuel consumed.")
        if nfs_book[car]['miles'] >= 100000:
            print(f"Time to sell the {car}!")
            del nfs_book[car]
    elif command == "Refuel":
        oil_kavkaz = int(data[2])
        diff = 75 - nfs_book[car]['brent']
        nfs_book[car]['brent'] += oil_kavkaz
        if nfs_book[car]['brent'] > 75:
            nfs_book[car]['brent'] = 75
            print(f"{car} refueled with {diff} liters")
        else:
            print(f"{car} refueled with {oil_kavkaz} liters")
    elif command == "Revert":
        kilometers = int(data[2])
        nfs_book[car]['miles'] -= kilometers
        if nfs_book[car]['miles'] < 10000:
            nfs_book[car]['miles'] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    text = input()


for brakma in nfs_book:
    print(f"{brakma} -> Mileage: {nfs_book[brakma]['miles']} kms, Fuel in the tank: {nfs_book[brakma]['brent']} lt.")