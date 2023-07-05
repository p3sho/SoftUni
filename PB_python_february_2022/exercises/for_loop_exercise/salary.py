tabs = int(input())
salary = int(input())
flag = False

for _ in range(tabs):
    open_tabs = input()

    if open_tabs == 'Facebook':
        salary -= 150
    elif open_tabs == 'Instagram':
        salary -= 100
    elif open_tabs == 'Reddit':
        salary -= 50

    if salary <= 0:
        flag = True
        break
if not flag:
    print(int(salary))
else:
    print('You have lost your salary.')