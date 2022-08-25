command = input()
is_completed = True
while command != "Welcome!":
    if command == "Voldemort":
        print("You must not speak of that name!")
        is_completed = False
        break
    if len(command) < 5:
        name = command
        print(f"{name} goes to Gryffindor.")
    elif len(command) == 5:
        name2 = command
        print(f"{name2} goes to Slytherin.")
    elif len(command) == 6:
        name3 = command
        print(f"{name3} goes to Ravenclaw.")
    elif len(command) > 6:
        name4 = command
        print(f"{name4} goes to Hufflepuff.")

    command = input()

if is_completed:
    print(f"Welcome to Hogwarts.")
# if command !=
# print(len(command))
