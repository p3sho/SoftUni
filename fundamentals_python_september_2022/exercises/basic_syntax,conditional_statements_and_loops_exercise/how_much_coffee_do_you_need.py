command = input()
number_of_coffees = 0
while command != 'END':
    if command in ['coding', 'dog', 'cat', 'movie']:
        number_of_coffees += 1
    elif command in ['CODING', 'DOG', 'CAT', 'MOVIE']:
        number_of_coffees += 2
    command = input()
if number_of_coffees > 5:
    print('You need extra sleep')
else:
    print(number_of_coffees)