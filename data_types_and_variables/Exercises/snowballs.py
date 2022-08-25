snowballs_num = int(input())
highest_snowballs_value = 0
best_weight = 0
best_time = 0
best_quality = 0
for snowball in range(snowballs_num):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    current_snowball_value = int((snowball_weight / snowball_time) ** snowball_quality)
    if current_snowball_value > highest_snowballs_value:
        highest_snowballs_value = current_snowball_value
        best_weight = snowball_weight
        best_time = snowball_time
        best_quality = snowball_quality



print(f"{best_weight} : {best_time} = {highest_snowballs_value} ({best_quality})")