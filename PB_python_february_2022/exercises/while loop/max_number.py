num = input()
max_num = -1000000000000

while num != 'Stop':
    sum = input()

    if sum > max_num:
        max_num =sum
    num = input()

print(max_num)