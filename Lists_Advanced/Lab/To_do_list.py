todo = ["" for i in range(11)]

command = input()

while command != "End":
    explore = command.split("-")
    priority = int(explore[0])
    note = explore[1]
    todo[priority] = note

    command = input()

todo_final = [task for task in todo if task != ""]

print(todo_final)