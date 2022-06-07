row_1 = int(input())
row_2 = int(input())
magic_number = int(input())
combination = False
count_number = 0
for number_1 in range(row_1, row_2 +1):
    for number_2 in range(row_1, row_2 +1):
        count_number += 1
        if number_1 + number_2 == magic_number:
            combination = True
            break
    if combination:
        break
if combination:
    print(f"Combination N:{count_number} ({number_1} + {number_2} = {magic_number})")

else:
    print(f"{count_number} combinations - neither equals {magic_number}")
