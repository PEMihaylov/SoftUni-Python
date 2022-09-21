phone_book = {}
while True:
    entry = input()
    if not "-" in entry:
        break
    name, phone = entry.split("-")
    phone_book[name] = phone
for checking in range(int(entry)):
    searched_contact = input()
    if searched_contact in phone_book.keys():   #or only in phone_book - like this it searches only in the keys
        print(f"{searched_contact} -> {phone_book[searched_contact]}")
    else:
        print(f"Contact {searched_contact} does not exist.")