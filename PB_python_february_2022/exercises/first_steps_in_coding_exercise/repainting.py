naylon = int(input())
boq_lt = int(input())
razreditel_lt = int(input())
hours = int(input())

price_naylon = (naylon + 2) * 1.5
price_boq = (boq_lt * 1.1) * 14.5
price_razreditel = razreditel_lt * 5
plikche = 0.40

price_mats = price_naylon + price_boq + price_razreditel + plikche
workers_price = (price_mats * 0.3) * hours
total_price = price_mats + workers_price

print(total_price)
