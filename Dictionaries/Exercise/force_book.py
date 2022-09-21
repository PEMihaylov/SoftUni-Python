# # from Chavdar...........................
def user_in_values(dict, name):
    for names in dict.values():
        if name in names:
            return True
    return False


def remove_user(dict, name):
    for users in dict.values():
        if name in users:
            users.remove(name)
    return dict


def change_side(dict, user, side):
    if side not in dict:
        dict[side] = []
    if user_in_values(dict, user):
        remove_user(dict, user)
    dict[side].append(user)
    print(f"{name} joins the {side} side!")
    return dict


def user_side(dict, name, side):
    if side not in dict:
        dict[side] = []
    if not user_in_values(dict, name):
        dict[side].append(name)
    return dict


force = {}
command = input()
while command != "Lumpawaroo":

    if "|" in command:
        side, name = command.split(" | ")
        users = user_side(force, name, side)
    elif "->" in command:
        name, side = command.split(" -> ")
        users = change_side(force, name, side)

    command = input()

for key, value in force.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for name in value:
            print(f"! {name}")


Ivan solution...........................................

force_side_dict = {}
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        splitted_command = command.split(" | ")
        force_side, force_user = splitted_command
        present = False
        for value in force_side_dict.values():
            if force_user in value:
                present = True
                break
        if not present:
            if force_side not in force_side_dict.keys():  # not in force_side_dict
                force_side_dict[force_side] = [force_user]
            else:
                force_side_dict[force_side].append(force_user)
    else: #elif "->" in command:
        splitted_command = command.split(" -> ")
        force_user, force_side = splitted_command
        for key, value in force_side_dict.items():
            if force_user in value:
                force_side_dict[key].pop(value.index(force_user))
                break
        if force_side not in force_side_dict.keys():
            force_side_dict[force_side] = [force_user]
        else:
            force_side_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()
for force_side in force_side_dict.keys():
    if len(force_side_dict[force_side]) > 0:
        print(f"Side: {force_side}, Members: {len(force_side_dict[force_side])}")
        [print(f"! {user}") for user in force_side_dict[force_side]]