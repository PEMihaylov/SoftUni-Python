student = input()
class_level = 1
skasan = 0
is_ejected = False
sum_class_grade = 0

while class_level <= 12:
    class_grade = float(input())
    if class_grade < 4:
        skasan += 1
        if skasan == 2:
            is_ejected = True
            break
        continue
    class_level += 1
    sum_class_grade += class_grade
if is_ejected:
    print(f"{student} has been excluded at {class_level} grade")
else:
    avg_grade = sum_class_grade / 12
    print(f"{student} graduated. Average grade: {avg_grade:.2f}")