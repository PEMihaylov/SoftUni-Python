length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = length * width * height

total_litres = volume / 1000
percent_lt = total_litres * (percent / 100)
needed_litres = total_litres - percent_lt

print(needed_litres)


