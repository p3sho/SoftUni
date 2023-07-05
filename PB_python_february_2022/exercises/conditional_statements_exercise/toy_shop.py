tour_price = float(input())
puzzels = int(input())
dolls = int(input())
bears = int(input())
minion = int(input())
trucks = int(input())

total_price = (puzzels * 2.60) + (dolls * 3) + \
              (bears * 4.10) + (minion * 8.20) + \
              (trucks * 2)

total_toys = puzzels + dolls + bears + minion + trucks

if total_toys >= 50:
    total_price -= total_price * 0.25

rent = total_price * 0.10
profit = total_price - rent

diff = abs(profit - tour_price)

if profit >= tour_price:
    print(f'Yes! {diff:.2f} lv left.')
else:
    print(f'Not enough money! {diff:.2f} lv needed.')
