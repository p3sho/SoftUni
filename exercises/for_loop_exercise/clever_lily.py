from math import floor
age = int(input())
peralnq_price = float(input())
toy_price = int(input())

toys = 0
saved_money = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        saved_money += 10 * (i / 2)
    else:
        toys += 1

stoled_money = floor(age / 2)
available_money = (toys * toy_price) + (saved_money - stoled_money)
diff = abs(available_money - peralnq_price)

if available_money >= peralnq_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')