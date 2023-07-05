budget = float(input())
statisti = int(input())
dress_price_for_one = float(input())

decor_price = budget * 0.10
dress_price = dress_price_for_one * statisti

if statisti > 150:
    dress_price -= dress_price * 0.10

total_sum = decor_price + dress_price
diff = abs(budget - total_sum)

if total_sum <= budget:
    print(f'Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')
else:
    print(f'Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')