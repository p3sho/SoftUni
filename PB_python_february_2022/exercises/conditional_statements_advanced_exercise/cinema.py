project = input()
rows = int(input())
columns = int(input())
income = 0
capacity = rows * columns

if project == 'Premiere':
    income = capacity * 12
elif project == 'Normal':
    income = capacity * 7.5
elif project == 'Discount':
    income = capacity * 5

print(f'{income:.2f} leva')