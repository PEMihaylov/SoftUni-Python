sum = 0
number = input()

while number != "NoMoreMoney":
    current_number = float(number)
    if current_number < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {current_number:.2f}")
    sum += current_number
    number = input()

print(f"Total: {sum:.2f}")