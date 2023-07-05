data = input().split(' ')
items = {}

for i in range(0, len(data), 2):
    key = data[i]
    value = data[i+1]
    items[key] = int(value)

print(items)