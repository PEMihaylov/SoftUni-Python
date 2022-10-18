N = int(input())

stack = []

for _ in range(N):
    command = input()

    if command.split()[0] == "1":
        stack.append(int(command.split()[1]))
    elif command == "2":
        if stack:
            stack.pop()
    elif command == "3":
        if stack:
            print(max(stack))
    elif command == "4":
        if stack:
            print(min(stack))


book = []
num = len(stack)
for _ in range(num):
    book.append(stack.pop())
print(", ".join(map(str, book)))

