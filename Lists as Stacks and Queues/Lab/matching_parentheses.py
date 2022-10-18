text = input()
stack = []
for idx in range(len(text)):
    if text[idx] == "(":
        stack.append(idx)
    elif text[idx] == ")":
        print(text[stack.pop():idx+1])
