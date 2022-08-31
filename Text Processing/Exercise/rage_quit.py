text = input().upper()
unique_symbols = ''
current_symbol = ''
repetitions = 0

for index in range(len(text)):
    if not text[index].isdigit():
        current_symbol += text[index]
    else: #symbol is digit - time to multiply
        for check_next_symbols in range(index, len(text)):
            if not text[check_next_symbols].isdigit():
                break
        repetitions = int(text[index])
        unique_symbols += repetitions * current_symbol
        current_symbol = ''
        repetitions = ''

print(f"Unique symbols used: {len(set(unique_symbols))}")
print(unique_symbols)


#................................................................

data = list(input())
strings = ""
numbers = ""

for index, char in enumerate(data):
    if char.isdigit():
        numbers += char
        strings == " "
    else:
        strings += char.upper()
        numbers += " "

strings = strings = strings.split()
numbers = numbers.split()

unique = len(set(''.join(strings)))

rage_message = ''.join(
    [f"{strings[i] * int(numbers[i])}" for i in range(len(strings))])

print(f"Unique symbols used: {unique}")
print(rage_message)

#.................................................................

data = input().upper()
text = ""
final_result = ""

for i in range(len(data)):
    number = ""
    char = data[i]

    if not char.isdigit():
        text += char

    else:
        if i + 1 < len(data) and data[i+1].isdigit():
            number = char + data[i+1]
        else:
            number = char
        final_result += text * int(number)
        text = ""

print(f"Unique symbols used: {len(set(final_result))}")
print(f"{final_result}")