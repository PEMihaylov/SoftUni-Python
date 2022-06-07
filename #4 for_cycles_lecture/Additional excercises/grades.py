number_of_students = int(input())

top_students = 0
very_good_students = 0
good_students = 0
bad_students = 0
total_grade = 0

for students in range(1, number_of_students + 1):
    grade = float(input())
    total_grade += grade
    if grade < 3.00:
        bad_students += 1
    elif grade < 4.00:
        good_students += 1
    elif grade < 5.00:
        very_good_students += 1
    else:
        top_students += 1

avg_top = top_students / number_of_students * 100
avg_very_good = very_good_students / number_of_students * 100
avg_good = good_students / number_of_students * 100
avg_bad = bad_students / number_of_students * 100
avg_grade = total_grade / number_of_students

print(f"Top students: {avg_top:.2f}%")
print(f"Between 4.00 and 4.99: {avg_very_good:.2f}%")
print(f"Between 3.00 and 3.99: {avg_good:.2f}%")
print(f"Fail: {avg_bad:.2f}%")
print(f"Average: {avg_grade:.2f}")
