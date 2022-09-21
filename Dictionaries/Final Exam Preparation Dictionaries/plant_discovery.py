number_of_plants = int(input())
plant_dict = {}

for num in range(number_of_plants):
    plants_info = input().split("<->")
    plant = plants_info[0]
    rarity = int(plants_info[1])
    if plant not in plant_dict:
        plant_dict[plant] = {'rarity': rarity, 'rating': []}
    else:
        plant_dict[plant]['rarity'] += rarity

text = input()
while text != "Exhibition":
    data = text.split(": ")
    command = data[0]
    new_data = data[1].split(" - ")

    if command == "Rate":
        plant_x = new_data[0]
        rating = int(new_data[1])
        if plant_x not in plant_dict:
            print("error")
        else:
            plant_dict[plant_x]["rating"].append(rating)
    elif command == "Update":
        plant_x = new_data[0]
        new_rarity = int(new_data[1])
        if plant_x not in plant_dict:
            print("error")
        else:
            plant_dict[plant_x]["rarity"] = new_rarity
    elif command == "Reset":
        plant_x = new_data[0]
        if plant_x not in plant_dict:
            print("error")
        else:
            plant_dict[plant_x]["rating"].clear()

    text = input()


print("Plants for the exhibition:")
for el in plant_dict:
    if len(plant_dict[el]['rating']) > 0 and sum(plant_dict[el]['rating']) > 0:
        print(f"- {el}; Rarity: {plant_dict[el]['rarity']}; Rating: {sum(plant_dict[el]['rating'])/len(plant_dict[el]['rating']):.2f}")
    else:
        print(f"- {el}; Rarity: {plant_dict[el]['rarity']}; Rating: 0.00")





#.......................................................






def create_plants_data(plants, number):
    for _ in range(number):
        data = input().split("<->")
        name_of_plant = data[0]
        rarity = int(data[1])

        if name_of_plant not in plants:
            plants[name_of_plant] = {'rarity': rarity, 'rating': []}
        else:
            plants[name_of_plant]['rarity'] += rarity

    return plants


def additional_plants_data(plants):

    while True:
        command = input().split(":")

        if command[0] == "Exhibition":
            break

        data = command[1].split(" - ")
        type_of_command = command[0]
        plant = data[0]

        if plant not in plants:
            print("error")
            continue

        if type_of_command == "Rate":
            rating = int(data[1])
            plants[plant]["rating"].append(rating)

        elif type_of_command == "Update":
            new_rarity = int(data[1])
            plants[plant]["rarity"] = new_rarity

        elif type_of_command == "Reset":
            plants[plant]["rating"].clear()

    return plants


def print_function(plants):
    print(f"Plants for the exhibition:")

    for dict_el in plants:
        if len(plants[dict_el]["rating"]) > 0 and sum(plants[dict_el]["rating"]) > 0:
            average_rating = sum(plants[dict_el]["rating"] / len(plants[dict_el]["rating"]))
            print(f"- {dict_el}; Rarity: {rarity}; Rating: {average_rating:.2f}")
        else:
            average_rating = 0
            rarity = plants[dict_el]["rating"]
            print(f"- {dict_el}; Rarity: {rarity}; Rating: {average_rating:.2f}")


def plant_discovery(number):
    plants = {}

    create_plants_data(plants, number)
    additional_plants_data(plants)
    print_function(plants)

n = int(input())
plant_discovery(n)

