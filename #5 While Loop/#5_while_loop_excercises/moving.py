width = int(input())
length = int(input())
height = int(input())
room_space = width * height * length

number_of_boxes = input()
while number_of_boxes != "Done":
    current_box = int(number_of_boxes)
    room_space -= current_box

    if room_space < 0:
        break
    number_of_boxes = input()

if room_space < 0:
    print(f"No more free space! You need {abs(room_space)} Cubic meters more.")
else:
    print(f"{room_space} Cubic meters left.")
