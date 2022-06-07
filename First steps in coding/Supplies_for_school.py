pens = int(input())

markers = int(input())

detergent_liters = int(input())

discount_inpercent = int(input())

# pens 5.80
# markers 7.20
# detergent 1.20

price_pens = pens - 5.80
price_markers = markers * 7.20
price_detergent = detergent_liters * 1.20

total_price = price_pens + price_markers + price_detergent

#print(total_price)

discount = total_price * (discount_inpercent / 100)
price_with_discount = total_price - discount
print(price_with_discount)