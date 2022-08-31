text = input()

while text != "end":
    rev = reversed(text)
    reversed_text = "".join(rev)
    print(f"{text} = {reversed_text}")

    text = input()

# .............................
string = input()

while string != "end":
    current_string = ""
    for i in reversed(string):
        current_string += i
    print(f{string} = {current_string}")

    string = input()

# ...........................
string = input()

while string != "end":
    current_string = ""
    for i in reversed(string):
        current_string += i
    print(string + " = " + current_string)

    string = input()