string_times = int(input())
is_pure_string = True

for check in range(string_times):
    current_string = input()
    check_str = str(current_string)
    for letter in check_str:
        if str(letter) != "_" and str(letter) != "," and str(letter) != ".":
            is_pure_string = True
        else:
            is_pure_string = False
            break

    if is_pure_string:
        print(f"{check_str} is pure.")

    else:
        print(f"{check_str} is not pure!")
