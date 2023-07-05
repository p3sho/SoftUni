paket_pens = int(input())
paket_markers = int(input())
lt_preparat = int(input())
procent_discount = int(input())

price_pens = paket_pens * 5.80
price_markers = paket_markers * 7.20
price_preparat = lt_preparat * 1.20

total_price = price_preparat + price_pens + price_markers
discount = total_price * (procent_discount / 100)
final_price = total_price - discount
print(final_price)