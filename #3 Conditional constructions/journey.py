budget = float(input())
season = input()

destination = ""
place = ""
expenses = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        expenses = budget * 0.30
    elif season == "winter":
        place = "Hotel"
        expenses = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place = "Camp"
    elif season == "winter":

elif budget > 1000:
    destination = "Europe"
    if season == "summer":
        place = "Camp"
    elif season == "winter":

