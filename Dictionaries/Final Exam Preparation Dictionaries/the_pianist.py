music_book = {}
numbers = int(input())

for song in range(numbers):
    info = input().split("|")
    curr_piece = info[0]
    curr_composer = info[1]
    curr_key = info[2]
    if curr_composer not in music_book:
        music_book[curr_piece] = []
    music_book[curr_piece] = [curr_composer, curr_key]

text = input()

while text != "Stop":
    data = text.split("|")
    command = data[0]

    if command == "Add":
        piece = data[1]
        composer = data[2]
        key = data[3]
        if piece in music_book.keys():
            print(f"{piece} is already in the collection!")
        else:
            music_book[piece] = []
            music_book[piece]= [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif command == "Remove":
        piece = data[1]
        if piece in music_book.keys():
            del music_book[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command == "ChangeKey":
        piece = data[1]
        new_key = data[2]
        if piece in music_book.keys():
            music_book[piece] = music_book[piece][:1] + [new_key] + music_book[piece][2:]
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    text = input()


for piece, composer in music_book.items():
    print(f"{piece} -> Composer: {composer[0]}, Key: {composer[1]}")



