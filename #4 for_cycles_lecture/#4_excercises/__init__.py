import math
n = int(input())
init_points = int(input())

points = 0
tournaments_won = 0

for i in range(1, n +1):
    round = input()
    if round == "W":
        points += 2000
        tournaments_won += 1
    elif round == "F":
        points += 1200
    elif round == "SF":
        points += 720

final_points = init_points + points
avg_points = math.floor(points / n)
percent_won = tournaments_won / n * 100

print(f"Final points: {final_points}")
print(f"Average points: {avg_points}")
print(f"{percent_won:.2f}%")
