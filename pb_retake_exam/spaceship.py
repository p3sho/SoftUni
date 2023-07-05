import math

shirochina = float(input())
duljina = float(input())
visochina = float(input())
astronavt_visochina = float(input())

raketa_obem = shirochina * visochina * duljina
obem_na_staq = (astronavt_visochina + 0.40) * 2 * 2
mqsto = math.floor(raketa_obem / obem_na_staq)

if 3 <= mqsto <= 10:
    print(f'The spacecraft holds {mqsto} astronauts.')
elif mqsto < 3:
    print('The spacecraft is too small.')
elif mqsto > 10:
    print('The spacecraft is too big.')