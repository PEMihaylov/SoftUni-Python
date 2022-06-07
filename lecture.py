import math
soap_opera = str(input())
length_opera = int(input())
break_time = int(input())

food_break = break_time / 8
relax_break = break_time / 4

diff = math.ceil(abs(break_time - length_opera - food_break - relax_break))

left_time = break_time - food_break - relax_break
if left_time > length_opera:
    print(f"You have enough time to watch {soap_opera} and left with {diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {soap_opera}, you need {diff} more minutes.")


