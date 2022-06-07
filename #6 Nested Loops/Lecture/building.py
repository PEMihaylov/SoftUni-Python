floor_number = int(input())
room_number = int(input())
letter = ""
for first_number in range(floor_number, 0, -1):
    for second_number in range(room_number):
        if first_number == floor_number:
            letter = "L"
        elif first_number % 2 != 0:
            letter = "A"
        elif first_number % 2 == 0:
            letter = "O"
        print(f"{letter}{first_number}{second_number}", end = " ")
    print()


