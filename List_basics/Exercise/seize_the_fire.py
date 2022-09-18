type_of_fires = input().split("#")
amount_of_water = int(input())
effort = 0
total_fire = 0
is_put_out = False

print("Cells:")
for command_line in type_of_fires:
    command_info = command_line.split(" = ")
    command = command_info[0]
    value = int(command_info[1])
    if amount_of_water >= value:
        if command == "High":
            if 81 <= value <= 125:
                is_put_out = True
                print(f"- {value}")
                amount_of_water -= value
                total_fire += value
                effort += value * 0.25

        elif command == "Medium":
            if 51 <= value <= 80:
                is_put_out = True
                print(f"- {value}")
                amount_of_water -= value
                total_fire += value
                effort += value * 0.25

        elif command == "Low":
            if 1 <= value <= 50:
                is_put_out = True
                print(f"- {value}")
                amount_of_water -= value
                total_fire += value
                effort += value * 0.25


print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
