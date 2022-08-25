num = int(input())
for char in range(0, num):
    for char_two in range(0, num):
        for char_three in range(0, num):
            i = chr(97 + char)
            j = chr(97 + char_two)
            k = chr(97 + char_three)
            result = i + j + k
            print(result)