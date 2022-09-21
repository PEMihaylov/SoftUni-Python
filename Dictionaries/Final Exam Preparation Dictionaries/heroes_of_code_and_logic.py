def create_heroes(heroes_dict, number):
    for _ in range(number):
        data = input().split(' ')
        hero_name = data[0]
        hit_points = int(data[1])
        mana_points = int(data[2])

        heroes_dict[hero_name] = [hit_points, mana_points]


def playing_game(heroes_dict):
    while True:
        command = input().split(' - ')

        if command[0] == 'End':
            break

        current_command = command[0]

        if current_command == 'CastSpell':
            hero_name = command[1]
            mp_needed = int(command[2])
            spell_name = command[3]
            available_mp = heroes_dict[hero_name][1]

            if available_mp >= mp_needed:
                heroes_dict[hero_name][1] -= mp_needed
                current_mp = heroes_dict[hero_name][1]
                print(f"{hero_name} has successfully cast {spell_name} and now has {current_mp} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")

        elif current_command == 'TakeDamage':
            hero_name = command[1]
            damage = int(command[2])
            attacker = command[3]
            available_hp = heroes_dict[hero_name][0]

            if available_hp - damage > 0:
                heroes_dict[hero_name][0] -= damage
                current_hp = heroes_dict[hero_name][0]

                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
            else:
                del heroes_dict[hero_name]
                print(f"{hero_name} has been killed by {attacker}!")

        elif current_command == 'Recharge':
            hero_name = command[1]
            amount = int(command[2])
            available_mp = heroes_dict[hero_name][1]

            if available_mp + amount > 200:
                amount = 200 - available_mp
                heroes_dict[hero_name][1] += amount
            else:
                heroes_dict[hero_name][1] += amount

            print(f"{hero_name} recharged for {amount} MP!")

        elif current_command == 'Heal':
            hero_name = command[1]
            amount = int(command[2])
            available_mp = heroes_dict[hero_name][0]

            if available_mp + amount > 100:
                amount = 100 - available_mp
                heroes_dict[hero_name][0] += amount
            else:
                heroes_dict[hero_name][0] += amount

            print(f"{hero_name} healed for {amount} HP!")

    return heroes_dict


def print_function(heroes_dict):
    for hero in heroes_dict:
        print(hero)
        print(f'  HP: {heroes_dict[hero][0]}')
        print(f'  MP: {heroes_dict[hero][1]}')


def heroes_of_code(number):
    # In heroes_dict we have list with two values:
    # HP - index 0, MP - index 1
    heroes_dict = {}

    create_heroes(heroes_dict, number)
    playing_game(heroes_dict)
    print_function(heroes_dict)


n = int(input())
heroes_of_code(n)


#....moeto reshenie..

num_of_heroes = int(input())
heroes_dict = {}
for n in range(num_of_heroes):
    text = input().split()
    hero_name = text[0]
    hit_p = int(text[1])
    mana_p = int(text[2])
    heroes_dict[hero_name] = {'HP': hit_p, 'MP': mana_p}

inline = input()
while inline != "End":
    data = inline.split(' - ')
    command = data[0]

    if command == "CastSpell":
        hero = data[1]
        mp_needed = int(data[2])
        spell_name = data[3]
        if heroes_dict[hero]['MP'] >= mp_needed:
            heroes_dict[hero]['MP'] -= mp_needed
            print(f"{hero} has successfully cast {spell_name} and now has {heroes_dict[hero]['MP']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif command == "TakeDamage":
        hero = data[1]
        damage = int(data[2])
        attacker = data[3]
        heroes_dict[hero]['HP'] -= damage
        if heroes_dict[hero]['HP'] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero]['HP']} HP left!")
        else:
            del heroes_dict[hero]
            print(f"{hero} has been killed by {attacker}!")
    elif command == "Recharge":
        hero = data[1]
        amount = int(data[2])
        diff = 200 - heroes_dict[hero]['MP']
        heroes_dict[hero]['MP'] += amount
        if heroes_dict[hero]['MP'] > 200:
            heroes_dict[hero]['MP'] = 200
            print(f"{hero} recharged for {diff} MP!")
        else:
            print(f"{hero} recharged for {amount} MP!")

    elif command == "Heal":
        hero = data[1]
        amount = int(data[2])
        diff = 100 - heroes_dict[hero]['HP']
        heroes_dict[hero]['HP'] += amount
        if heroes_dict[hero]['HP'] > 100:
            heroes_dict[hero]['HP'] = 100
            print(f"{hero} healed for {diff} HP!")
        else:
            print(f"{hero} healed for {amount} HP!")


    inline = input()

for heroes in heroes_dict:
    print(f"{heroes}")
    print(f"  HP: {heroes_dict[heroes]['HP']}")
    print(f"  MP: {heroes_dict[heroes]['MP']}")