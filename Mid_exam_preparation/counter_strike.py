energy = int(input())
won_battle_counter = 0

while True:
    command = input()

    if command == "End of battle":
        print(f"Won battles: {won_battle_counter}. Energy left: {energy}")
        break

    distance = int(command)

    if energy >= distance:
        energy -= distance
        won_battle_counter += 1

        if won_battle_counter % 3 == 0:
            energy += won_battle_counter
    else:
        print(f"Not enough energy! Game ends with {won_battle_counter} won battles and {energy} energy")
        break


#...........
initial_energy = int(input())
won_battles = 0

distance = input()
is_game_won = True
while distance != "End of battle":
    curr_distance = int(distance)
    if initial_energy < curr_distance:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
        is_game_won = False
        break
    else:
        won_battles += 1

        initial_energy -= curr_distance
        if won_battles % 3 == 0:
            initial_energy += won_battles

    distance = input()

if is_game_won:
    print(f"Won battles: {won_battles}. Energy left: {initial_energy}")