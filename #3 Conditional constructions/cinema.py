screening_type = input()
rows = int(input())
columns = int(input())

price = 0
seat_capacity = rows * columns

if screening_type == "Premiere":
    price = 12
elif screening_type == "Normal":
    price = 7.5
elif screening_type == "Discount":
    price = 5.00

sum = price * seat_capacity

print(f"{sum:.2f} leva")