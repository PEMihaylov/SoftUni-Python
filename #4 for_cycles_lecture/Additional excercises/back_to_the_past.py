money_inherited = float(input())
end_year = int(input())
spend_money = 0
current_age = 18
money_left = 0
for year in range(1800, end_year + 1):
    if year % 2 == 0:
        spend_money += 12000
    elif year % 2 != 0:
        spend_money = spend_money + 12000 + (50 * current_age)
    current_age += 1
    money_left = money_inherited - spend_money
diff = abs(money_inherited - spend_money)
if money_inherited - spend_money >= 0:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")