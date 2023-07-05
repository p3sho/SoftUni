number_of_stings = int(input())
non_pure_symbols = ['.', ',', '_']
pureness = True

for sting in range(number_of_stings):
    data_check = input()
    for symbol in non_pure_symbols:
        if symbol in data_check:
            pureness = False
    if pureness:
        print(f'{data_check} is pure.')
    else:
        print(f'{data_check} is not pure!')
    pureness = True 