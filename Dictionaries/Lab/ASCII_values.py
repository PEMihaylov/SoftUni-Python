characters = input().split(", ")
char_dict = {char:ord(char) for char in characters}

print(char_dict)


# char_dict = dict()
#
# for char in characters:
#     char_dict[char] = ord(char)

info = input().split(", ")
dictionary = {info[i]: ord(info[i]) for i in range(len(info))}
print(dictionary)