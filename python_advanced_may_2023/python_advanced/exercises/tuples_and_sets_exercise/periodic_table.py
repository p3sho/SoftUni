n = int(input())
chemicals = set()

for _ in range(n):
    elements = input().split()
    for element in elements:
        chemicals.add(element)

print('\n'.join(chemicals))