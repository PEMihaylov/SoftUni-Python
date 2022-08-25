divisor = int(input())
boundary = int(input())
largest_integer = 0
for cycle in range(1, boundary + 1):
    if cycle % divisor == 0 and cycle <= boundary:
        largest_integer = cycle
print(largest_integer)
