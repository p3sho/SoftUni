temp = int(input())
time = input()
outfit = ""
shoes = ""

if time == 'Morning':
    if 10 <= temp <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < temp <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 24 < temp:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
if time == 'Afternoon':
    if 10 <= temp <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < temp <= 24:
        outfit = "T-Shirt"
        shoes = 'Sandals'
    elif 24 < temp:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
if time == 'Evening':
    if 10 <= temp <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < temp <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 24 < temp:
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {temp} degrees, get your {outfit} and {shoes}.")