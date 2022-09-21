def password_reset():
    data = input()

    while True:
        command = input().split()

        if command[0] == "Done":
            print(f"Your password is: {data}")
            break
        elif command[0] == "TakeOdd":
            data = ''.join([data[i] for i in range(len(data)) if i % 2 != 0])
            print(data)
        elif command[0] == "Cut":
            index = int(command[1])
            length = int(command[2])
            data = ''.join([data[i] for i in range(len(data)) if i < index or i >= index + length])
            print(data)
        elif command[0] == "Substitute":
            substring = command[1]
            substitute = command[2]
            if substring in data:
                data = data.replace(substring, substitute)  #.. do => not data.replace(substring, substitute)
                print(data)
            else:
                print("Nothing to replace!")


password_reset()



#..........moeto, ama , abe....

password = input()
text = input()

while text != "Done":
    data = text.split()
    command = data[0]
    if command == "TakeOdd":
        password = "".join([password[i] for i in range(len(password)) if i % 2 != 0])
        print(password)
    elif command == "Cut":
        index = int(data[1])
        length = int(data[2])
        password = password[:index] + password[index + length:]
        print(password)
    elif command == "Substitute":
        substring = data[1]
        substitute = data[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    text = input()

print(f"Your password is: {password}")