target_sum = int(input())

gained_sum = 0
command_line = input()
while command_line != "closed":
    service_type = str(command_line)
    command = str(input())
    if service_type == "haircut":
        if command == "mens":
            gained_sum += 15
        elif command == "ladies":
            gained_sum += 20
        elif command == "kids":
            gained_sum += 10

    if service_type == "color":
        if command == "touch up":
            gained_sum += 20
        elif command == "full color":
            gained_sum += 30

    if gained_sum >= target_sum:
        break
    command_line = input()

diff = abs(gained_sum - target_sum)

if gained_sum >= target_sum:
    print("You have reached your target for the day!")
    print(f"Earned money: {gained_sum}lv.")
else:
    print(f"Target not reached! You need {diff}lv. more.")
    print(f"Earned money: {gained_sum}lv.")