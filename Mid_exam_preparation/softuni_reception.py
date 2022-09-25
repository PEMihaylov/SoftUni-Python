efficiency_one = int(input())
efficiency_two = int(input())
efficiency_three = int(input())
students_count = int(input())
total_time = 0
students_per_hour = efficiency_one + efficiency_two + efficiency_three
waiting_students = students_count
break_count = 0

while waiting_students:
    total_time += 1
    break_count += 1
    waiting_students -= students_per_hour
    if waiting_students <= 0:
        break

    if break_count % 3 == 0:
        total_time += 1
        break_count = 0

print(f"Time needed: {total_time}h.")

