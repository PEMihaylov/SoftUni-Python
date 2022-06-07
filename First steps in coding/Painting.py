nylon = int(input())
paint = int(input())
razr = int(input())
hours_workers = int(input())

price_nylon = (nylon + 2) * 1.5
price_paint = (paint *1.10) * 14.50
price_razr = razr * 5

sum = price_nylon + price_paint + price_razr + 0.40

sum_workers = (sum * 0.30) * hours_workers

total_sum = sum + sum_workers
print(total_sum)