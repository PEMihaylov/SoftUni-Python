number = int(input())
result_count = 0
for real_number in range(number+1):
    for real_number_2 in range(number+1):
        for real_number_3 in range(number+1):
           result = real_number + real_number_2 + real_number_3
           if result == number:
               result_count += 1
print(result_count)