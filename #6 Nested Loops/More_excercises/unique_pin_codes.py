number_one = int(input())
number_two = int(input())
number_three = int(input())
is_prime = False
for cycle in range(1, number_one + 1):
    if cycle % 2 == 0:
        print(cycle, end=" ")
    else:
        continue
    for cycle_two in range(2, 8):
        if cycle_two > number_two or cycle_two == 4 or cycle_two ==6:
            break
        else:
            if cycle_two == 2 or cycle_two == 3 or cycle_two == 5 or cycle_two == 7:
                print(cycle_two, end=" ")

        for cycle_three in range(1, number_three +1):

            if cycle_three % 2 == 0:
                print(cycle_three, end=" ")
                print()
            else:
                continue
            print(cycle, end=" ")
            print(cycle_two, end=" ")

