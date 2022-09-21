text = input()
courses = dict()

while ":" in text:

    # (name, id, course) = text.split(":")
    data = text.split(":")
    name = data[0]
    id = data[1]
    course = data[2]

    if course not in courses.keys():
        courses[course] = dict()

    courses[course][id] = name

    text = input()

text = text.replace("_", " ")

if text in courses.keys():
    for id in courses[text]:
        print(f"{courses[text][id]} - {id}")

# for id in courses[text]:
#     print(f"{courses[text][id]} - {id}")




students_dict = {}
command = input()
while ":" in command:
    info = command.split(":")
    name, id, course = info[0], info[1], info[2]
    if course not in students_dict:
        students_dict[course] = {}
    students_dict[course][id] = name
    command = input()

course = " ".join(command.split("_"))
for key, value in students_dict.items():
    if key == course:
        for id, name in value.items():
            print(f'{name} - {id}')
