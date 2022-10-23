from collections import deque

seats = input().split(", ")
seq_deque = deque([int(k) for k in input().split(", ")])
seq_stack = deque([int(k) for k in input().split(", ")])
taken_seats = []
rotation = 0

while rotation < 10 and len(taken_seats) < 3:
    rotation += 1
    front_num = seq_deque.popleft()
    back_num = seq_stack.pop()
    sum_chr = chr(front_num + back_num)

    combo_one = str(front_num) + sum_chr
    combo_two = str(back_num) + sum_chr

    if combo_one in seats:
        taken_seats.append(combo_one)
        seats.remove(combo_one)

    elif combo_two in seats:
        taken_seats.append(combo_two)
        seats.remove(combo_two)

    else:
        seq_deque.append(front_num)
        seq_stack.appendleft(back_num)

print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotation}")
