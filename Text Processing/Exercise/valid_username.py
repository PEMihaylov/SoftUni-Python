# usernames = input().split(", ")
# for username in usernames:
#     username_is_valid = True
#     if not 3 <= len(username) <= 16:
#         username_is_valid = False
#         continue
#     for character in username:
#         if not(character.isalnum() or character == "-" or character == "-"):
#             username_is_valid = False
#             continue
#     if ' ' in username:
#         username_is_valid = False
#     if username_is_valid: # if username is valid == True
#         print(username)


#....................................
def lenght_is_valid(username):
    if 3 <= len(username) <= 16:
        return True
    return False

def characters_are_valid(username):
    for character in username:
        if not (character.isalnum() or character == "-" or character == "-"):
            return False
        return True

def no_redundant_symbols(username):
    if ' ' in username:
        return False
    return True


usernames = input().split(", ")
for username in usernames:
    if lenght_is_valid(username) and characters_are_valid(username) and no_redundant_symbols(username):
        print(username)


#...............................

def lenght_is_valid(username):
    if 3 <= len(username) <= 16:
        return True
    return False

def characters_are_valid(username):
    for character in username:
        if not (character.isalnum() or character == "-" or character == "-"):
            return False
        return True

def no_redundant_symbols(username):
    if ' ' in username:
        return False
    return True

def username_is_valid(username):
    if lenght_is_valid(username) and characters_are_valid(username) and no_redundant_symbols(username):
        return True
    return False

usernames = input().split(", ")
for username in usernames:
    if username_is_valid(username):
        print(username)