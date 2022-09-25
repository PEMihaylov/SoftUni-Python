journal = input().split(", ")
text = input()
while text != "Craft!":
    data = text.split(" - ")
    command = data[0]
    item = data[1]
    if command == "Collect":
        if item not in journal:
            journal.append(item)
    elif command == "Drop":
        if item in journal:
            journal.remove(item)
    elif command == "Combine Items":
        old_item = item.split(":")[0]
        new_item = item.split(":")[1]
        if old_item in journal:
            i = journal.index(old_item)
            journal.insert(i + 1, new_item)
    elif command == "Renew":
        if item in journal:
            journal.remove(item)
            journal.insert(len(journal), item)
    text = input()

print(", ".join(journal))