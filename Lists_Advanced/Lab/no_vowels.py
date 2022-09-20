# vowels = ["a", "o", "u", "e", "i"]
# text = input()
# no_vowels_text = list()
#
# for ch in text:
#     if ch not in vowels:
#         no_vowels_text.append(ch)
#
#
# print("".join(no_vowels_text))


# vowels = ["a", "o", "u", "e", "i"]
# text = input()
# no_vowels_text = [ch for ch in text if ch not in vowels]
#
# print("".join(no_vowels_text))


text = input()
vowels = ['a', 'o', 'u', 'e', 'i']

result = [letter for letter in text if letter.lower() not in vowels]

print(''.join(result))