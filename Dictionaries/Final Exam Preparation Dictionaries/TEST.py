# # pattern = r"([@\*])([A-Z][a-z]{2,})\1\:\s((\[([A-Za-z])\]\|){3})$"
#
# import re
#
# pattern = r"([@\*])([A-Z][a-z]{2,})\1\:\s\[([A-Za-z])\]\|\[([A-Za-z])\]\|\[([A-Za-z])\]\|$"
# msg = input()
#
#
# matches = re.search(pattern, msg)
#
# print(matches)
# tag = matches[2]
# number_one = matches[3]
# number_two = matches[4]
# number_three = matches[5]
# print(f"{tag}: {ord(number_one)} {ord(number_two)} {ord(number_three)}")

# x = ['a', 'a', 'a']
# x.extend(['s', 'b'])
# z = 'fsdf'
# x.pop()
# z.pop
b = {"name"="geore","age"=22}
z = dict({"sd":"dfd"}, age=22)
print(b)