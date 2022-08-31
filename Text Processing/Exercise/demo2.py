# text = input()
#
# for ch in range(len(text)):
#     if text[ch] == ":" and text[ch+1] != " ":
#         emoticon = text[ch] + text[ch + 1]
#         print(emoticon)

def emoticon_finder(text):
    emoticon = [text[ch] + text[ch + 1] for ch in range(len(text)) if text[ch] == ":" and text[ch + 1] != " "]
    print('\n'.join(emoticon))

text = input()

emoticon_finder(text)
