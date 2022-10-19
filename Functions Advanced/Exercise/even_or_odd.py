def even_odd(*command):

    if command[-1] == "even":
        final_list = [int(n) for n in command[:-1] if n % 2 == 0]
    elif command[-1] == "odd":
        final_list = [int(n) for n in command[:-1] if n % 2 != 0]

    return final_list


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))