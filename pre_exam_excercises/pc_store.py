number_of_games = int(input())
hearthstone_count = 0
fornite_count = 0
overwatch_count = 0
others_count = 0

for games in range(number_of_games):
    game = str(input())
    if game == "Hearthstone":
        hearthstone_count += 1
    elif game == "Fornite":
        fornite_count += 1
    elif game == "Overwatch":
        overwatch_count += 1
    else:
        others_count += 1

sales_percent_hearthstone = hearthstone_count / number_of_games * 100
sales_percent_fornite = fornite_count / number_of_games * 100
sales_percent_overwatch = overwatch_count / number_of_games * 100
sales_percent_others = others_count / number_of_games * 100

print(f"Hearthstone - {sales_percent_hearthstone:.2f}%")
print(f"Fornite - {sales_percent_fornite:.2f}%")
print(f"Overwatch - {sales_percent_overwatch:.2f}%")
print(f"Others - {sales_percent_others:.2f}%")
