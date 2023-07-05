food_in_grams = float(input()) * 1000
hay_in_grams = float(input()) * 1000
cover_in_grams = float(input()) * 1000
guineas_weight_in_grams = float(input()) * 1000


for days in range(1, 31):
    food_in_grams -= 300

    if days % 2 == 0:
        hay_in_grams -= food_in_grams * 0.05
    if days % 3 == 0:
        cover_in_grams -= guineas_weight_in_grams / 3

if cover_in_grams <= 0 or hay_in_grams <= 0 or food_in_grams <= 0:
    print('Merry must go to the pet store!')
else:
    print(f'Everything is fine! Puppy is happy! Food: {food_in_grams/1000:.2f}, Hay: {hay_in_grams/1000:.2f}, Cover: {cover_in_grams/1000:.2f}.')