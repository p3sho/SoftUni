names = int(input())

name_list = set()

for _ in range(names):
    name = input()
    name_list.add(name)

for name in name_list:
    print(name)
