items = input().split('!')
data = input()

while data != 'Go Shopping!':
    if 'Correct' in data:
        _, old_item, new_item = data.split()
        if old_item in items:
            items[items.index(old_item)] = new_item
        data = input()
        continue

    command, item = data.split()

    if command == 'Urgent':
        if item not in items:
            items.insert(0, item)

    elif command == 'Unnecessary':
        if item in items:
            items.remove(item)

    elif command == 'Rearrange':
        if item in items:
            items.remove(item)
            items.append(item)

    data = input()

print(*items, sep=', ')