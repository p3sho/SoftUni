n = int(input())
names = set()

for _ in range(n):
    username = input()
    names.add(username)

print(*names, sep='\n')