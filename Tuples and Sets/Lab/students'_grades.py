count = int(input())
students = {}
for _ in range(count):
    data = tuple(input().split())
    stud, grade = data
    if stud not in students:
        students[stud] = []
    students[stud].append(float(grade))

for key, value in students.items():
    trans = [str(f"{i:.2f}") for i in value]
    print(f"{key} -> {' '.join(trans)} (avg: {sum(value)/len(value):.2f})")
