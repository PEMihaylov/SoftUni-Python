def get_name(names: tuple, letter: str):
    for name in names:
        if name.startswith(letter):
            return name


def age_assignment(*names, **kwargs):
    people = {}
    result = ''

    for key, value in kwargs.items():
        name = get_name(names, key)
        people[name] = value

    sorted_people = dict(sorted(people.items(), key=lambda x: x[0]))

    for name, age in sorted_people.items():
        result += f"{name} is {value} years old." + '\n'

    return result



#.....my solution...............

# def age_assignment(*args, **kwargs):
#     result = ''
#     kwargs = dict(sorted(kwargs.items(), key=lambda x: x[0]))
#     for key, value in kwargs.items():
#         for name in args:
#             if name[0] == key:
#                 result += f"{name} is {value} years old." + '\n'
#
#     return result
#
#
print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))