number_one = int(input())
number_two = int(input())
for cycle_one in range(number_one, number_two +1):
    even_sum = 0
    odd_sum = 0
    current_number = str(cycle_one)
    for index in range(0, len(current_number)):
        digit = int(current_number[index])
        if index % 2 != 0:
            odd_sum += digit
        else:
            even_sum += digit

    if even_sum == odd_sum:
        print(current_number, end=" ")