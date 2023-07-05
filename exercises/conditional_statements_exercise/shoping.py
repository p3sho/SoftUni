budget = float(input())
videocards = int(input())
procesors = int(input())
ram = int(input())

videocard_price = videocards * 250

procesor_price = videocard_price * 0.35
sum_procesors = procesor_price * procesors

ram_price = videocard_price * 0.10
sum_ram = ram_price * ram

total_price = videocard_price + sum_procesors + sum_ram

if videocards >= procesors:
    total_price -= total_price * 0.15

diff = abs(budget - total_price)

if budget >= total_price:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')