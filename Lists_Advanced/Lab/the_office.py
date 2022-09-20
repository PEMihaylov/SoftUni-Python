employees = input().split(" ")
employees = list(map(int, employees))
factor = int(input())

happy_employees = list(filter(lambda emp: emp >= sum(employees) / len(employees), employees))

if len(happy_employees) >= len(employees) / 2:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are not happy!")

#..................................................................

employees = input().split()
factor = int(input())
employees = list(map(lambda x: int(x) * factor, employees))
average = sum(employees)/len(employees)
happy_list = []
for emp in employees:
    if emp >= average:
        happy_list.append(emp)
if len(happy_list) >= len(employees)/2:
    print(f"Score: {len(happy_list)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(happy_list)}/{len(employees)}. Employees are not happy!")