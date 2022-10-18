text = input()

occurrences_tuple = {}

for letter in text:
    if letter not in occurrences_tuple:
        occurrences_tuple[letter] = 0
    occurrences_tuple[letter] += 1

for i in sorted(occurrences_tuple.keys()):
    print(f"{i}: {occurrences_tuple[i]} time/s")


# text = input()

# [print(f"{symbol}: {symbol.count}") for symbol in sorted(set(text))]

