def start_spring(**fauna):
    new_fauna = {}
    result = []

    for name, type in fauna.items():
        if type not in new_fauna:
            new_fauna[type] = []
        new_fauna[type].append(name)

    new_fauna = dict(sorted(new_fauna.items(), key=lambda x: (-len(x[1]), x[0])))

    for key, value in new_fauna.items():
        curr_result = ""
        curr_result += key + ":" + "\n"
        curr_result += "-" + "\n-".join(sorted(value))
        result.append(curr_result)

    return '\n'.join(result)

#
# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower",}
# print(start_spring(**example_objects))
#
# # #
# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))
# #
#
example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
