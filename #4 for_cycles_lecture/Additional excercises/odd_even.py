import sys

num = int(input())
odd_sum = 0
odd_min = sys.maxsize
odd_max = - sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = - sys.maxsize

for pos in range(1, num + 1):
    current_num = float(input())
    if pos % 2 != 0:
        odd_sum += current_num
        if current_num < odd_min:
            odd_min = current_num

        if current_num > odd_max:
            odd_max = current_num

    elif pos % 2 == 0:
        even_sum += current_num
        if current_num < even_min:
            even_min = current_num

        if current_num > even_max:
            even_max = current_num

print(f"OddSum={odd_sum:.2f},")
if odd_sum == 0:
    print(f"OddMin=No,")
    print(f"OddMax=No,")
else:
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
print(f"EvenSum={even_sum:.2f},")
if even_sum == 0:
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
else:
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
