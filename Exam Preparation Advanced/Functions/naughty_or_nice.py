def naughty_or_nice_list(names, *shuffle, **kwargs):
    santa_list = {}

    for num in names:
        if num[0] not in santa_list.keys():
            santa_list[num[0]] = []
        santa_list[num[0]].append(num[1])

    new_santa = {}

    for item in shuffle:
        count, type = item.split("-")
        if type not in new_santa.keys():
            if len(santa_list[int(count)]) == 1:
                new_santa[type] = santa_list[int(count)]
                santa_list[int(count)].clear()


    for kid, behavior in kwargs.items():
        if behavior not in new_santa.keys():
            new_santa[behavior] = []
        new_santa[behavior].append(kid)



    return santa_list
#
print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

# #
# # print(naughty_or_nice_list(
# #     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
#     ))
#
#
# print(naughty_or_nice_list(
#     [
#         (6, "John"),
#         (4, "Karen"),
#         (2, "Tim"),
#         (1, "Merry"),
#         (6, "Frank"),
#     ],
#     "6-Nice",
#     "5-Naughty",
#     "4-Nice",
#     "3-Naughty",
#     "2-Nice",
#     "1-Naughty",
#     Frank="Nice",
#     Merry="Nice",
#     John="Naughty",
# ))
#
