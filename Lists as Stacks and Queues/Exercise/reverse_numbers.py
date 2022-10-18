text = list(map(int, input().split()))
reversed_text = []

for _ in range(len(text)):
    reversed_text.append(text.pop())

print(*reversed_text)

#..............................


text = list(map(int, input().split()))

for _ in range(len(text)):
    print(text.pop(), end=" ")











