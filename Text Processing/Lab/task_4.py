banned = input().split(", ")
text = input()

for word in banned:
    while word in text:
        text = text.replace(word, "*" * len(word))

print(text)

#..........

banned = input().split(", ")
text = input()

while True:
    for ch in banned:
        if ch in text:
            text = text.replace(ch, len(ch)*"*")
    else:
        break
print(text)

