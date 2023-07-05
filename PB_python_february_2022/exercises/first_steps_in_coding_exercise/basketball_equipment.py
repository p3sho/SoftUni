tax_per_year = int(input())

shoes = tax_per_year - (tax_per_year * 0.4)
clothes = shoes - (shoes * 0.2)
ball = clothes / 4
accs = ball / 5

total_price = tax_per_year + shoes + clothes + ball + accs

print(total_price)