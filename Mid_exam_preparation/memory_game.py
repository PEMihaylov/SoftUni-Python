elements = input().split()
moves = 0
while True:
    integers = input()
    if integers == "end":
        if len(elements) > 0:
            print("Sorry you lose :(")
            print(' '.join([str(x) for x in elements]))
            break
    moves += 1
    data = integers.split()
    index_one = int(data[0])
    index_two = int(data[1])

    if index_one == index_two or index_one < 0 or index_two < 0 or index_one >= len(elements) or index_two >= len(elements):
        elements.insert(int(len(elements)/2), "-" + str(moves) + "a")
        elements.insert(int(len(elements)/2), "-" + str(moves) + "a")
        print("Invalid input! Adding additional elements to the board")
    elif elements[index_one] == elements[index_two]:
        if index_one > index_two:
            removed_item = elements.pop(index_two)
            elements.pop(index_one - 1)

        else:
            removed_item = elements.pop(index_one)
            elements.pop(index_two - 1)
        print(f"Congrats! You have found matching elements - {removed_item}!")
    elif elements[index_one] != elements[index_two]:
        print("Try again!")

    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        break



#..........

def is_valid_index(index, list_length):
    return 0 <= index < list_length


items = input().split()

command_input = input()
moves_counter = 0
is_won = False

while command_input != "end":
    command_args = command_input.split()
    index_one = int(command_args[0])
    index_two = int(command_args[1])
    moves_counter += 1

    if index_one != index_two and not is_valid_index(index_one, len(items)) or not is_valid_index(index_two,
                                                                                                  len(items)):
        new_item = f"-{moves_counter}a"
        middle_index = len(items) // 2
        items.insert(middle_index, new_item)
        items.insert(middle_index, new_item)
        print("Invalid input! Adding additional elements to the board")
        command_input = input()
        continue

    if items[index_one] != items[index_two]:
        print("Try again!")
        command_input = input()
        continue

    removed_item = items.pop(index_one)
    items.remove(removed_item)
    print(f"Congrats! You have found matching elements - {removed_item}!")

    if len(items) == 0:
        is_won = True
        break

    command_input = input()

if is_won:
    print(f"You have won in {moves_counter} turns!")
else:
    print(f"Sorry you lose :(")
    print(" ".join(items))

#..................

sequence_of_elements = input().split(" ")
moves_count = 0

while True:
    elements = input().split(" ")
    if "end" in elements:
        if len(sequence_of_elements) > 0:  # Проверка дали не сме загубили играта след "end"
            print("Sorry you lose :(")
            print(" ".join(sequence_of_elements))
            break
        else:
            break
    elements = [int(x) for x in elements]  # Парсване на елементите към int
    moves_count += 1
    if elements[0] == elements[1] or 0 > elements[0] or elements[0] >= len(sequence_of_elements) \
            or 0 > elements[1] or elements[1] >= len(sequence_of_elements):  # Проверка дали играча не лъже
        sequence_of_elements.insert(int(len(sequence_of_elements) / 2), f"-{moves_count}a")  # Добавяне ба елементи в средата на тестето
        sequence_of_elements.insert(int(len(sequence_of_elements) / 2), f"-{moves_count}a")
        print("Invalid input! Adding additional elements to the board")

    elif sequence_of_elements[elements[0]] == sequence_of_elements[elements[1]]:  # Попадение и премахваме елементи
        max_elements = max(sequence_of_elements[elements[0]], sequence_of_elements[elements[1]])
        min_elements = min(sequence_of_elements[elements[0]], sequence_of_elements[elements[1]])

        sequence_of_elements.remove(min_elements)
        sequence_of_elements.remove(max_elements)
        print(f"Congrats! You have found matching elements - {max_elements}!")
    elif sequence_of_elements[elements[0]] != sequence_of_elements[elements[1]]:  # Проверка за грешно попадение
        print("Try again!")

    if len(sequence_of_elements) == 0:  # Проверка дали елементите в тестето не са свършили и приключваме играта ако е вярно
        print(f"You have won in {moves_count} turns!")
        break

