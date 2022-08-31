# version 1
import itertools


def jackpot(t):
    for s in symbols:
        if s in ticket and ticket.count(s) == 20:
            print(f'ticket "{ticket}" - 10{s} Jackpot!')
            return True
    return False


def win_ticket(t):
    left = ticket[:10]
    right = ticket[10:]
    for s, i in itertools.product(symbols, range(9, 5, -1)):
        if s * i in left and s * i in right:
            print(f'ticket "{ticket}" - {i}{s}')
            return True
    return False


data = [x.strip() for x in input().split(", ")]
symbols = ['@', '#', '$', '^']

for ticket in data:
    if len(ticket) == 20:
        if jackpot(ticket):
            continue
        if not win_ticket(ticket):
            print(f'ticket "{ticket}" - no match')
        continue
    else:
        print('invalid ticket')


#..........................

def count_symbols(side, symbol):
    current_count = 0
    total_count = []
    for i in range(len(side)):
        if symbol == side[i]:
            current_count += 1
            if i == len(side) - 1:
                total_count.append(current_count)
        else:
            total_count.append(current_count)
            current_count = 0
    return max(total_count)


def search_func(data, symbols):
    first_side, second_side = data[:10], data[10:]
    for symbol in symbols:
        if symbol * 6 in first_side and symbol * 6 in second_side:
            counter = min((count_symbols(first_side, symbol)), count_symbols(second_side, symbol))
            return f'ticket "{data}" - {counter}{symbol}'
    else:
        return f'ticket "{data}" - no match'


def check_ticket(data):
    pattern = ['@', '#', '$', '^']
    for ticket in data:
        if len(ticket) != 20:
            print("invalid ticket")
        elif ticket[0] in pattern and ticket.count(ticket[0]) == 20:
            print(f'ticket "{ticket}" - {10}{ticket[0]} Jackpot!')
        else:
            print(search_func(ticket, pattern))


tickets = [x.strip() for x in input().split(", ")]
check_ticket(tickets)
