n_number = int(input())
number = n_number * 2
counter = 0
sum = 0
for sequence_number in range(1, number + 1):
    current_number = int(input())
    if sequence_number % 2 != 0:
        sum += current_number
        counter += 1
    elif sequence_number % 2 == 0:
        sum += current_number
        counter += 1

    if counter >= 2:
        pair_sum = sum






