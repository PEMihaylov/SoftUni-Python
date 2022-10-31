def print_row(figure_size, row_size):
    print(' ' * (num - row), end='')
    for col in range(1, row + 1):
        print("* ", end="")
    print()


num = int(input())

for row in range(1, num + 1):
    print_row(num, row)

for row in range(num - 1, -1, -1):
    print_row(num, row)
