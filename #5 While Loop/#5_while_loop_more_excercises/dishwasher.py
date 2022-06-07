number_of_detergent = int(input())

detergent_volume = number_of_detergent * 750
load_counter = 0
number_of_clean_dishes = 0
number_of_clean_pans = 0

number_of_appliances = input()
while number_of_appliances != "End":
    load_counter += 1
    type_of_appliances = int(number_of_appliances)
    if load_counter % 3 != 0:
        number_of_clean_dishes += type_of_appliances
        dish_volume = type_of_appliances * 5
        detergent_volume -= dish_volume
    elif load_counter % 3 == 0:
        number_of_clean_pans += type_of_appliances
        pan_volume = type_of_appliances * 15
        detergent_volume -= pan_volume

    if detergent_volume < 0:
        break
    number_of_appliances = input()

if detergent_volume >= 0:
    print("Detergent was enough!")
    print(f"{number_of_clean_dishes} dishes and {number_of_clean_pans} pots were washed.")
    print(f"Leftover detergent {detergent_volume} ml.")
else:
    print(f"Not enough detergent, {abs(detergent_volume)} ml. more necessary!")
