number = int(input())
academy = {}
# student = ""
for num in range(1, (number*2) +1):
    data = input()
    if num % 2 != 0:
        student = data
        if student not in academy:
            academy[student] = [0]

    elif num % 2 == 0:
        grade = float(data)
        if student not in academy:
            academy[student] += grade
        academy[student].append(grade)

for stud in academy:
    if 0 in academy[stud]:
        academy[stud].remove(0)


for i in academy.keys():
    avg = sum(academy[i]) / len(academy[i])
    academy[i] = avg


for i in academy:
    if academy[i] >= 4.50:
        print(f"{i} -> {academy[i]:.2f}")


