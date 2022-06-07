command_line = input()

prime_numbers_sum = 0
non_prime_numbers_sum = 0

while command_line != "stop":
    number = int(command_line)
    if number < 0:
        print("Number is negative.")
        command_line = input()
        continue

    count = 0
    for iter in range(1, number +1):
        if number % iter == 0:
            count += 1
    if count == 2:
        prime_numbers_sum += number
    else:
        non_prime_numbers_sum += number

    command_line = input()

print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")