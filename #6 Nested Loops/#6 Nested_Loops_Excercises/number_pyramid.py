number = int(input())
count = 1
is_bigger_n = False
for row in range(1, number + 1):
    for column in range(1, row + 1):
        if count > number:
            is_bigger_n = True
            break
    print(count, end=" ")

