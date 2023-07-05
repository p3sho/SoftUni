bought_food_in_kg = int(input())
condition = False
counter = 0
while True:
    food_in_g_per_meal = input()
    if food_in_g_per_meal == 'Adopted':
        condition = True
        break
    counter += int(food_in_g_per_meal)
diff = abs(counter - (bought_food_in_kg * 1000))
if condition:
    if bought_food_in_kg * 1000 >= counter:
        print(f"Food is enough! Leftovers: {diff} grams.")
    elif counter > bought_food_in_kg * 1000:
        print(f"Food is not enough. You need {diff} grams more.")