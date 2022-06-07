number_of_cakes = int(input())
box_of_eggs = int(input())
kg_of_cookies = int(input())

price_of_cakes = number_of_cakes * 3.20
price_of_eggs = box_of_eggs * 4.35
price_of_cookies = kg_of_cookies * 5.40
price_of_paint = box_of_eggs * 12 * 0.15

total_spend = price_of_cakes + price_of_eggs + price_of_cookies + price_of_paint

print(f"{total_spend:.2f}")