inline = input()
pirates_book = {}
while inline != "Sail":
    text = inline.split('||')
    city = text[0]
    population = int(text[1])
    gold = int(text[2])
    if city not in pirates_book.keys():
        pirates_book[city] = {'popul': population, 'goldy': gold}
    else:
        pirates_book[city]['popul'] += population
        pirates_book[city]['goldy'] += gold

    inline = input()

string = input()
while string != "End":
    data = string.split('=>')
    command = data[0]
    town = data[1]
    if command == "Plunder":
        people = int(data[2])
        gold_pl = int(data[3])
        print(f"{town} plundered! {gold_pl} gold stolen, {people} citizens killed.")
        pirates_book[town]['popul'] -= people
        pirates_book[town]['goldy'] -= gold_pl
        if pirates_book[town]['popul'] == 0 or pirates_book[town]['goldy'] == 0:
            del pirates_book[town]
            print(f"{town} has been wiped off the map!")
    elif command == "Prosper":
        gold_pr = int(data[2])
        if gold_pr <= 0:
            print("Gold added cannot be a negative number!")
        else:
            pirates_book[town]['goldy'] += gold_pr
            print(f"{gold_pr} gold added to the city treasury. {town} now has {pirates_book[town]['goldy']} gold.")

    string = input()

if len(pirates_book) > 0:
    print(f"Ahoy, Captain! There are {len(pirates_book)} wealthy settlements to go to:")
    for place in pirates_book:
        print(f"{place} -> Population: {pirates_book[place]['popul']} citizens, Gold: {pirates_book[place]['goldy']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")