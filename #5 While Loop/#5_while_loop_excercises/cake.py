length = int(input())
width = int(input())
total_pieces = length * width

input_cake = input()

while input_cake != "STOP":
    current_cake = int(input_cake)
    total_pieces -= current_cake

    if total_pieces <= 0:
        break
    input_cake = input()

if total_pieces > 0:
    print(f"{total_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
