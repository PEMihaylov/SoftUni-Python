tour_initial = input()
text = input()
tour = tour_initial
while text != "Travel":
    data = text.split(":")
    command = data[0]
    if command == "Add Stop":
        index = int(data[1])
        string = data[2]
        if 0 <= index < len(tour):
            tour = tour[:index] + string + tour[index:]
            print(tour)
        else:
            print()
    elif command == "Remove Stop":
        start_index = int(data[1])
        end_index = int(data[2])
        if 0 <= start_index < len(tour) and 0 <= end_index < len(tour):
            tour = tour[:start_index] + tour[end_index + 1:]
            print(tour)
        else:
            print(tour)
    elif command == "Switch":
        old_string = data[1]
        new_string = data[2]
        if old_string in tour_initial:
            tour = tour.replace(old_string, new_string)
            print(tour)
        else:
            print(tour)

    text = input()

print(f"Ready for world tour! Planned stops: {tour}")