train_wagons = int(input())
train = [0] * train_wagons
command = input()


def add_people(people):
    train[-1] = train[-1] + people


def insert_people(wagon, number_people):
    train[wagon] = train[wagon] + number_people


def leave_people(wagon, number_people):
    train[wagon] = train[wagon] - number_people


while command != "End":
    command, *info = [int(x) if x.isdigit() else x for x in command.split()]

    if "add" in command:
        people = info[0]
        add_people(people)
    else:
        index, people = info
        if "insert" in command:
            insert_people(index, people)

        elif "leave" in command:
            leave_people(index, people)

    command = input()

print(train)