from collections import deque

result = True
parentheses = deque(input())
stack = []
num = len(parentheses)

for sign in range(num):
    if parentheses[0] in ["{", "[", "("]:
        stack.append(parentheses.popleft())

    elif parentheses[0] == "}":
        if stack and stack[-1] == "{":
            stack.pop()
            parentheses.popleft()
            result = True
        else:
            result = False
            break

    elif parentheses[0] == ")":
        if stack and stack[-1] == "(":
            stack.pop()
            parentheses.popleft()
            result = True
        else:
            result = False
            break

    elif parentheses[0] == "]":
        if stack and stack[-1] == "[":
            stack.pop()
            parentheses.popleft()
            result = True
        else:
            result = False
            break


if not result:
    print("NO")
else:
    print("YES")