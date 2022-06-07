num_of_students = int(input())

top_students = 0
very_good_students = 0
good_students = 0
failed_students = 0
grade_sum = 0

for student in range(num_of_students):
    grade = float(input())
    current_grade = grade
    grade_sum += current_grade
    if current_grade >= 5.00:
        top_students += 1
    elif 4.00 <= current_grade < 5.00:
        very_good_students += 1
    elif 3.00 <= current_grade < 4.00:
        good_students += 1
    elif current_grade < 3.00:
        failed_students += 1


top_students_percent = top_students / num_of_students * 100
very_good_student_percent = very_good_students / num_of_students * 100
good_students_percent = good_students / num_of_students * 100
failed_students_percent = failed_students / num_of_students * 100
avg_grade_sum = grade_sum / num_of_students

print(f"Top students: {top_students_percent:.2f}%")
print(f"Between 4.00 and 4.99: {very_good_student_percent:.2f}%")
print(f"Between 3.00 and 3.99: {good_students_percent:.2f}%")
print(f"Fail: {failed_students_percent:.2f}%")
print(f"Average: {avg_grade_sum:.2f}")