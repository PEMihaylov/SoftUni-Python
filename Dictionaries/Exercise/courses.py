text = input()

courses = {}
while text != "end":

    course_name, student_name = text.split(" : ")

    if course_name not in courses.keys():
        courses[course_name] = [student_name]

    else:
        courses[course_name].append(student_name)

    text = input()

for course in courses:
    print(f"{course}: {len(courses[course])}")
    for student in courses[course]:
        print(f"-- {student}")