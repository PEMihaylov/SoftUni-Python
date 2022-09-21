letters = {}
symbols = ''.join(s for s in input().split())
for letter in symbols:
    if letter not in letters.keys():
        letters[letter] = 0
    letters[letter] += 1
print(letters)
exit()
for key, value in letters.items():
    print(f"{key} -> {value}")

# for key in letters.keys():
#     print(f"{key} -> {value}")