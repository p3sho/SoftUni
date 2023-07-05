n = int(input())
m = int(input())
s = int(input())
number = 0

for i in range(m, n - 1, -1):
    if i % 2 == 0 and i % 3 == 0:
        if i == s:
            break
        print(f'{i}', end=' ')