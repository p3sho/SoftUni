cats = int(input())
group1 = 0
group2 = 0
group3 = 0
grams = 0

for i in range(1, cats + 1):
    g_food = float(input())
    grams += g_food
    if 100 <= g_food < 200:
        group1 += 1
    elif 200 <= g_food < 300:
        group2 += 1
    elif 300 <= g_food < 400:
        group3 += 1

food_price_per_day = (grams / 1000) * 12.45
print(f'Group 1: {group1} cats.')
print(f'Group 2: {group2} cats.')
print(f'Group 3: {group3} cats.')
print(f'Price for food per day: {food_price_per_day:.2f} lv.')