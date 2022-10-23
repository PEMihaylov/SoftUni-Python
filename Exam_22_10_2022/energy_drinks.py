from collections import deque

caffeine = [int(x) for x in input().split(', ')]
drinks = deque([int(x) for x in input().split(', ')])

stamat_drunk = 0
total_caffeine = 0

while caffeine and drinks:
    caffe = caffeine.pop()
    drink = drinks.popleft()
    if (caffe * drink) + stamat_drunk <= 300:
        stamat_drunk += caffe * drink
        total_caffeine += caffe * drink
    else:
        drinks.append(drink)
        stamat_drunk -= 30
        if stamat_drunk < 0:
            stamat_drunk = 0

if drinks:
    print(f"Drinks left: {', '.join(map(str, drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat_drunk} mg caffeine.")