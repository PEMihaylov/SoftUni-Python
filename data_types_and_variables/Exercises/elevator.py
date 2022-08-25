number_people = int(input())
capacity = int(input())

rest = number_people % capacity
courses = int(number_people // capacity)
if rest > 0:
    courses += 1

print(courses)