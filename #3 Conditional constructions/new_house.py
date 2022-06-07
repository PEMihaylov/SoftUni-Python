type_flower = input()
count_flower = int(input())
budget = int(input())

sum = 0

if type_flower == "Roses":
    sum = 5 * count_flower
    if count_flower > 80:
        sum = sum * 0.90
elif type_flower == "Dahlias":
    sum = 3.80 * count_flower
    if count_flower > 90:
        sum = sum * 0.85
elif type_flower == "Tulips":
    sum = 2.80 * count_flower
    if count_flower > 80:
        sum = sum * 0.85
elif type_flower == "Narcissus":
    sum = 3 * count_flower
    if count_flower < 120:
        sum = sum * 1.15
elif type_flower == "Gladiolus":
    sum = 2.50 * count_flower
    if count_flower < 80:
        sum = sum * 1.20

diff = abs(budget - sum)

if budget >= sum:
    print(f"Hey, you have a great garden with {count_flower} {type_flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")