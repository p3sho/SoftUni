party_price = float(input())
love = int(input())
rose = int(input())
keyholder = int(input())
karikatura = int(input())
luck_suprise = int(input())

total_sum = (love * 0.60) + (rose * 7.20) + (keyholder * 3.60) + (karikatura * 18.20) + (luck_suprise * 22)
artikuls_sum = love + rose + keyholder + karikatura + luck_suprise

if artikuls_sum >= 25:
    total_sum -= total_sum * 0.35
else:
    total_sum = total_sum
win_money = total_sum - (total_sum * 0.10)

if win_money >= party_price:
    print(f'Yes! {win_money - party_price:.2f} lv left.')
else:
    diff = party_price - win_money
    print(f'Not enough money! {diff:.2f} lv needed.')
