text = input()
digits = ""
letters = ""
symbols = ""

for ch in text:
    if ch.isdigit():
        digits += ch
    elif ch.isupper() or ch.islower():
        letters += ch
    else:
        symbols += ch

print(digits)
print(letters)
print(symbols)


#............
text = input()

final_digit = ""
final_string = ""
final_ch = ""
for ch in text:
    if ch.isdigit():
        final_digit += ch
    elif ch.isalpha():
        final_string += ch
    else:
        final_ch += ch

print(final_digit)
print(final_string)
print(final_ch)