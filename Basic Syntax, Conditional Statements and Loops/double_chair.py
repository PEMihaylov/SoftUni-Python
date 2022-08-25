# command = input()
# while command != "End":
#     new_str = ''
#     for letter in command:
#         new_str += letter * 2
#     if command != "SoftUni":
#         print(new_str)
#     command = input()



command = input()
while command != "End":
    if command == "SoftUni":
        command = input()
    new_str = ''
    for letter in command:
        new_str += letter * 2
    print(new_str)
    command = input()