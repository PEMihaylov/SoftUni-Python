bad_mark = int(input())
task_name = str(input())
bad_count = 0
score = 0
task_count = 0
new_task_name = ''
while task_name != "Enough":
    mark = int(input())
    score += mark
    task_count += 1
    new_task_name = task_name

    if mark <= 4:
        bad_count += 1

    if bad_mark == bad_count:
        print(f"You need a break, {bad_count} poor grades.")
        break
    task_name = str(input())

avg_score = score / task_count

if task_name == "Enough":
    print(f"Average score: {avg_score:.2f}")
    print(f"Number of problems: {task_count}")
    print(f"Last problem: {new_task_name}")

# poor_grades = int(input())
#
# sum_grades = 0
# count_grades = 0
# last_problem = ""
# count_poor_grades = 0
# has_failed = False
# input_line = input()
# while input_line != "Enough":
#     grade = int(input())
#     if grade <= 4:
#         count_poor_grades += 1
#
#     last_problem = input_line
#     count_grades = count_grades + 1
#     sum_grades = sum_grades + grade
#
#     if poor_grades == count_poor_grades:
#         has_failed = True
#         break
#     input_line = input()
#
# if has_failed:
#     print(f"You need a break, {count_poor_grades} poor grades.")
# else:
#     avg_grades = sum_grades / count_grades
#     print(f"Average score: {avg_grades:.2f}")
#     print(f"Number of problems: {count_grades}")
#     print(f"Last problem: {last_problem}")