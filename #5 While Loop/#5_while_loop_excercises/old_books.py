# book = str(input())
# new_book = str(input())
# n = 0
#
# while new_book != "No More Books":
#     if book != new_book:
#         n += 1
#     else:
#         print(f"You checked {n} books and found it.")
#         break
#     new_book = str(input())
#
# if new_book == "No More Books":
#     print(f"The book you search is not here!")
#     print(f"You checked {n} books.")


book = str(input())
new_book = str(input())
n = 0
is_found = False

while new_book != "No More Books":
    if book == new_book:
        is_found = True
        print(f"You checked {n} books and found it.")
        break
    else:
        n += 1
        new_book = input()

if not is_found:
    print(f"The book you search is not here!")
    print(f"You checked {n} books.")


