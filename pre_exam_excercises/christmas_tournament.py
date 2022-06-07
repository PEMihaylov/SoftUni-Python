number_of_days = int(input())
total_win_count = 0
total_lose_count = 0
total_money = 0
for days in range(number_of_days):
    win_count = 0
    loses_count = 0
    money = 0
    command = input()
    while command != "Finish":
        result = str(input())
        if result == "win":
            win_count += 1
            total_win_count += 1
            money += 20
        elif result == "lose":
            loses_count += 1
            total_lose_count +=1
        command = str(input())

    if win_count > loses_count:
        money = money * 1.10
    total_money += money
if total_win_count > total_lose_count:
    total_money = total_money * 1.20

if total_win_count > total_lose_count:
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
elif total_win_count < total_lose_count:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
