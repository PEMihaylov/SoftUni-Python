message = input()
text = input()
while text != "Decode":

    data = text.split("|")
    command = data[0]

    if command == "Move":
        num_of_letters = int(data[1])
        message = message[num_of_letters:] + message[:num_of_letters]
    elif command == "Insert":
        index = int(data[1])
        value = data[2]
        message = message[:index] + value + message[index:]

    elif command == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        message = message.replace(substring, replacement)

    text = input()

print(f"The decrypted message is: {message}")