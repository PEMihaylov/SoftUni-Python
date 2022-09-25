quarter = list(map(int, input().split("@")))
text = input()
position = 0
while text != "Love!":
    data = text.split()
    index = int(data[1])
    if index + position >= len(quarter):
        position = 0
    else:
        position += index
    if quarter[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        quarter[position] -= 2
        if quarter[position] == 0:
            print(f"Place {position} has Valentine's day.")
    text = input()

print(f"Cupid's last position was {position}.")
if sum(quarter) == 0:
    print("Mission was successful.")
else:
    houses = len([num for num in quarter if num != 0])
    print(f"Cupid has failed {houses} places.")