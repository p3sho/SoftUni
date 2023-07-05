def create_healing_items(textiles, medicaments):
    healing_items = {
        "Patch": 30,
        "Bandage": 40,
        "MedKit": 100
    }

    created_items = {}

    while textiles and medicaments:
        textile = textiles.pop(0)
        medicament = medicaments.pop()

        total = textile + medicament

        if total in healing_items.values():
            for item, value in healing_items.items():
                if value == total:
                    created_items[item] = created_items.get(item, 0) + 1
                    break
        elif total > healing_items["MedKit"]:
            created_items["MedKit"] = created_items.get("MedKit", 0) + 1
            medicaments[-1] += total - healing_items["MedKit"]
        else:
            textiles.append(textile)
            medicaments.insert(0, medicament + 10)

    if not textiles and not medicaments:
        print("Textiles and medicaments are both empty.")
    elif not textiles:
        print("Textiles are empty.")
    else:
        print("Medicaments are empty.")

    sorted_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))
    for item, count in sorted_items:
        print(f"{item} - {count}")

    if medicaments:
        print("Medicaments left:", ", ".join(str(x) for x in medicaments[::-1]))
    if textiles:
        print("Textiles left:", ", ".join(str(x) for x in textiles))

# Example usage
textiles_input = input()
medicaments_input = input()

textiles = [int(x) for x in textiles_input.split()]
medicaments = [int(x) for x in medicaments_input.split()]

create_healing_items(textiles, medicaments)
