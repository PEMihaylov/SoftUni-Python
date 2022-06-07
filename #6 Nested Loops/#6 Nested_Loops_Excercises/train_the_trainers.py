# total_assessment = 0
# number_of_presentations = 0
# command = input()
# while command != "Finish":
#     num_of_jury = int(command)
#     presentation_grades = 0
#     presentation = str(input())
#     number_of_presentations += 1
#     for grade in range(num_of_jury):
#         assessment = float(input())
#         presentation_grades += assessment
#
#     avg_presentations_grade = presentation_grades / num_of_jury
#
#     print(f"{presentation} - {avg_presentations_grade}.")
#     total_assessment += avg_presentations_grade
#     command = input()
#
# total_avg_assessment = total_assessment / number_of_presentations
# # print(f"Student's final assessment is {total_avg_assessment}.")

command = int(input())
number_of_presentations = 0
presentation = str(input())
total_assessment = 0

while presentation != "Finish":
    number_of_presentations += 1
    presentation_grades = 0
    for grade in range(command):
        jury_assessment = float(input())
        presentation_grades += jury_assessment
    avg_presentations_grade = presentation_grades / command
    total_assessment += avg_presentations_grade
    print(f"{presentation} - {avg_presentations_grade:.2f}.")

    presentation = str(input())

total_avg_assessment = total_assessment / number_of_presentations
print(f"Student's final assessment is {total_avg_assessment:.2f}.")