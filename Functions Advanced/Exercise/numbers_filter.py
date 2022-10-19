def even_odd_filter(**command):
    numbers = {}

    for key, value in command.items():
        if key == 'odd':
            numbers[key] = [int(x) for x in value if x % 2 != 0]

        elif key == 'even':
            numbers[key] = [int(x) for x in value if x % 2 == 0]

    return dict(sorted(numbers.items(), key=lambda x: (len(x[1])), reverse=True))


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
