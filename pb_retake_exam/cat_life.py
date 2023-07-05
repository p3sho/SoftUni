import math

cat_model = input()
sex = input()

if cat_model == 'British Shorthair':
    if sex == 'm':
        human_months = 13 * 12
        cat_months = math.floor(human_months / 6)
    elif sex == 'f':
        human_months = 14 * 12
        cat_months = math.floor(human_months / 6)
    print(f'{cat_months} cat months')
elif cat_model == 'Siamese':
    if sex == 'm':
        human_months = 15 * 12
        cat_months = math.floor(human_months / 6)
    elif sex == 'f':
        human_months = 16 * 12
        cat_months = math.floor(human_months / 6)
    print(f'{cat_months} cat months')
elif cat_model == 'Persian':
    if sex == 'm':
        human_months = 14 * 12
        cat_months = math.floor(human_months / 6)
    elif sex == 'f':
        human_months = 15 * 12
        cat_months = math.floor(human_months / 6)
    print(f'{cat_months} cat months')
elif cat_model == 'Ragdoll':
    if sex == 'm':
        human_months = 16 * 12
        cat_months = math.floor(human_months / 6)
    elif sex == 'f':
        human_months = 17 * 12
        cat_months = math.floor(human_months / 6)
    print(f'{cat_months} cat months')
elif cat_model == 'American Shorthair':
    if sex == 'm':
        human_months = 12 * 12
        cat_months = math.floor(human_months / 6)
    elif sex == 'f':
        human_months = 13 * 12
        cat_months = math.floor(human_months / 6)
    print(f'{cat_months} cat months')
elif cat_model == 'Siberian':
    if sex == 'm':
        human_months = 11 * 12
        cat_months = math.floor(human_months / 6)
    elif sex == 'f':
        human_months = 12 * 12
        cat_months = math.floor(human_months / 6)
    print(f'{cat_months} cat months')
else:
    print(f'{cat_model} is invalid cat!')

