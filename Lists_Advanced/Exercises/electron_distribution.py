num = int(input())
shells = []
x_num = 1
curr_num = num
while curr_num > 0:
    digit = 2 * (x_num**2)
    if digit > curr_num:
        shells.append(curr_num)
        break
    shells.append(digit)
    x_num += 1
    curr_num -= digit

print(shells)

