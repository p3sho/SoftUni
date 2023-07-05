spell = [input()]


def check_index(index_):
    if 0 <= index_ < len(spell[0]):
        return True
    print("The spell was too weak.")


def illusion(index_, letter):
    if check_index(index_):
        spell[0] = spell[0][:index_] + letter + spell[0][index_ + 1:]
        print("Done!")


def divination(first_substring, second_substring):
    if first_substring in spell[0]:
        spell[0] = spell[0].replace(first_substring, second_substring)
        print(spell[0])


def alteration(substring):
    if substring in spell[0]:
        spell[0] = spell[0].replace(substring, "", 1)
        print(spell[0])


possible_commands = ["Abracadabra", "Abjuration", "Necromancy", "Illusion", "Divination", "Alteration"]

commmand = input()

while commmand != "Abracadabra":
    asked_command = commmand.split()

    if asked_command[0] not in possible_commands:
        print("The spell did not work!")

    else:
        if asked_command[0] == "Abjuration":
            spell[0] = spell[0].upper()
            print(spell[0])

        elif asked_command[0] == "Necromancy":
            spell[0] = spell[0].lower()
            print(spell[0])

        elif asked_command[0] == "Illusion":
            illusion(int(asked_command[1]), asked_command[2])

        elif asked_command[0] == "Divination":
            divination(asked_command[1], asked_command[2])

        elif asked_command[0] == "Alteration":
            alteration(asked_command[1])

    commmand = input()