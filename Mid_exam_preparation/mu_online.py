rooms = input().split("|")
health = 100
bitcoins = 0
is_alive = True
place = 0
for room in rooms:
    place += 1
    data = room.split()
    command = data[0]
    value = int(data[1])
    if command != "potion" and command != "chest":
        health -= value
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {place}")
            is_alive = False
            break
    elif command == "potion":
        health += value
        if health > 100:
            healed = abs(health - 100 - value)
            health = 100
        else:
            healed = value
        print(f"You healed for {healed} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")

if is_alive:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
