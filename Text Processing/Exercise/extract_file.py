path = input().split("\\")
filename, extension = path[-1].split(".")
print(f"File name: {filename}")
print(f"File extension: {extension}")

#.................

text = input().split("\\")

for ch in text:
    if "." in ch:
        file_name, file_extension = ch.split(".")
    else:
        continue

    print(f"File name: {file_name}")
    print(f"File extension: {file_extension}")