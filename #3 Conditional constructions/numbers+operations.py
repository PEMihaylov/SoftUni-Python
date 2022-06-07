N1 = int(input())
N2 = int(input())
Operator = input()

if (Operator == "/" or Operator == "+" or Operator == "*" or Operator == "/" or Operator == "%") and N2 == 0:
    print(f"Cannot divide {N1} by zero")
elif Operator == "+":
    result = N1 + N2
    if result % 2 == 0:
        number = "even"
    elif result % 2 != 0:
        number = "odd"
    print(f"{N1} {Operator} {N2} = {result} - {number}")
elif Operator == "-":
    result = N1 - N2
    if result % 2 == 0:
        number = "even"
    elif result % 2 != 0:
        number = "odd"
    print(f"{N1} {Operator} {N2} = {result} - {number}")
elif Operator == "*":
    result = N1 * N2
    if result % 2 == 0:
        number = "even"
    elif result % 2 != 0:
        number = "odd"
    print(f"{N1} {Operator} {N2} = {result} - {number}")
elif Operator == "/":
    result = N1 / N2
    print(f"{N1} / {N2} = {result:.2f}")
elif Operator == "%":
    result = N1 % N2
    print(f"{N1} % {N2} = {result}")

