text = input()
stud_book = {}
submissions = []
while text != "exam finished":
    data = text.split("-")
    student = data[0]
    language = data[1]
    if language != "banned":
        submissions.append(language)
    if language != "banned":
        points = int(data[2])
        is_bigger = False
        if student not in stud_book:
            stud_book[student] = {}
            stud_book[student][language] = points
        if student in stud_book.keys():
            for key in stud_book[student].keys():
                if key == language:
                    if stud_book[student][language] < points:
                        stud_book[student][language] = points
                    else:
                        continue
    else:
        del stud_book[student]

    text = input()

print("Results:")
for key, value in stud_book.items():
    for lang, score in value.items():
        print(f"{key} | {score}")

print("Submissions:")
res = {}
for i in submissions:
    res[i] = submissions.count(i)
for key, value in res.items():
    print(f"{key} - {value}")
