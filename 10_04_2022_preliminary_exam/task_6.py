num = int(input())
is_combination_valid = False

for a in range(1, 10):
    if is_combination_valid:
        break
    for b in range(9, a-1, -1):
        if is_combination_valid:
            break
        for c in range(0, 10):
            if is_combination_valid:
                break
            for d in range(9, c-1, -1):
                if (a + b + c + d) == (a * b * c * d) and num % 10 == 5:
                    is_combination_valid = True
                    if is_combination_valid:
                        print(f"{a}{b}{c}{d}")
                        break
                elif (a * b * c * d) // (a + b + c + d) == 3 and num % 3 == 0:
                    is_combination_valid = True
                    if is_combination_valid:
                        print(f"{d}{c}{b}{a}")
                        break
if not is_combination_valid:
    print("Nothing found")