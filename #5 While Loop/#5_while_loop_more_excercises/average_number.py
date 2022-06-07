number = int(input())
count = 0
sum = 0
while number > count:
    new_number = int(input())
    sum += new_number
    count += 1
    avg_sum = sum / number

print(f"{avg_sum:.2f}")

