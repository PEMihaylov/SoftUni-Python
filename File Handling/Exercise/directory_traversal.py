import os

directory = input()
extensions = {}


for file in os.listdir(directory):
    file_x = os.path.join(directory, file)

    if os.path.isfile(file_x):
        ext = file.split(".")[-1]

        if ext not in extensions:
            extensions[ext] = []
        extensions[ext].append(file)


extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    print(f".{extension}")
    for filename in sorted(files):
        print(f"---{filename}")