needed_money = float(input())
initial_money = float(input())
days = 0
count_spend = 0
total_money = initial_money

while total_money < needed_money:
    if count_spend == 5:
        break
    days += 1
    action = str(input())
    current_money = float(input())
    if action == "save":
        count_spend = 0
        total_money += current_money
    elif action == "spend":
        total_money -= current_money
        count_spend += 1
        if total_money < 0:
            total_money = 0

if count_spend == 5:
    print(f"You can't save the money.")
    print(days)

else:
    print(f"You saved the money for {days} days.")








