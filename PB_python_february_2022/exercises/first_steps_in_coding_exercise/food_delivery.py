chicken_menus = int(input())
fish_menus = int(input())
vegan_menus = int(input())

chicken_price = chicken_menus * 10.35
fish_price = fish_menus * 12.40
vegan_price = vegan_menus * 8.15
total_price = chicken_price + fish_price + vegan_price
desert = total_price * 0.2

final_price = total_price + desert + 2.50
print(final_price)