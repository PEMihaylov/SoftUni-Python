event = input()
number_of_coffee = 0
while event != "END":
    if event == "coding" or event == "CODING" or event == "dog" or event == "DOG" or event == "cat" or event == "CAT" or event == "movie" or event == "MOVIE":
        for letter in event:
            if letter.isupper():
                number_of_coffee += 2
                break
            else:
                number_of_coffee += 1
                break

    event = input()
if number_of_coffee <= 5:
    print(number_of_coffee)
else:
    print("You need extra sleep")