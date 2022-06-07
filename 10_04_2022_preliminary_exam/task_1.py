paper_rolls_count = int(input())
clothes_rolls_count = int(input())
glue_litres = float(input())
discount = int(input())

price_paper = paper_rolls_count * 5.80
price_clothes = clothes_rolls_count * 7.20
price_glue = glue_litres * 1.20

total_price = (price_glue + price_paper + price_clothes) * (1 - discount/100)

print(f"{total_price:.3f}")