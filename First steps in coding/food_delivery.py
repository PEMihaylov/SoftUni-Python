chicken_menu_count = int(input())
fish_menu_count = int(input())
veg_menu_count = int(input())

# Брой пилешки менюта – цяло число в интервала [0 … 99]
#  Брой менюта с риба – цяло число в интервала [0 … 99]
#  Брой вегетариански менюта – цяло число в интервала [0 … 99]

price_chicken_menu = chicken_menu_count * 10.35
price_fish_menu = fish_menu_count * 12.4
price_veg_menu = veg_menu_count * 8.15

all_menu_sum = price_veg_menu + price_fish_menu + price_chicken_menu

dessert = all_menu_sum * 0.20
total_sum = all_menu_sum + dessert + 2.50
print(total_sum)