num = int(input())

car_book = {}
for user in range(num):
    data = input().split()
    command = data[0]
    if command == "register":
        username = data[1]
        plate = data[2]
        if username not in car_book.keys():
            car_book[username] = plate
            print(f"{username} registered {plate} successfully")
        else:
            if plate in car_book[username]:
                print(f"ERROR: already registered with plate number {plate}")


    elif command == "unregister":
        command = data[0]
        username = data[1]
        if username not in car_book.keys():
            print(f"ERROR: user {username} not found")
        else:
            del car_book[username]
            print(f"{username} unregistered successfully")

for key, value in car_book.items():
    print(f"{key} => {value}")