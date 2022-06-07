contract_period = str(input())
contract_type = str(input())
mobile_net = str(input())
months_paid = int(input())

monthly_plan = 0
total_paid = 0
total_months = 0
if contract_period == "one":
    if contract_type == "Small":
        monthly_plan = 9.98
    elif contract_type == "Middle":
        monthly_plan = 18.99
    elif contract_type == "Large":
        monthly_plan = 25.98
    elif contract_type == "ExtraLarge":
        monthly_plan = 35.99
elif contract_period == "two":
    if contract_type == "Small":
        monthly_plan = 8.58
    elif contract_type == "Middle":
        monthly_plan = 17.09
    elif contract_type == "Large":
        monthly_plan = 23.59
    elif contract_type == "ExtraLarge":
        monthly_plan = 31.79

if mobile_net == "yes":
    if monthly_plan <= 10.00:
        monthly_plan += 5.50
    elif monthly_plan <= 30.00:
        monthly_plan += 4.35
    elif monthly_plan > 30.00:
        monthly_plan += 3.85

total_paid = monthly_plan * months_paid

if contract_period == "two":
    total_paid = total_paid * (1 - 0.0375)


print(f"{total_paid:.2f} lv.")