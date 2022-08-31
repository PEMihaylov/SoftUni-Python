text = input()
# text = text.replace(" ", "")
final_text = ""

for ch in text:
    word = chr(int(str(ord(ch)+3)))
    final_text += word
print(final_text)