def solve_challenge(tools, substances, challenges):
    while tools and substances:
        tuuls = tools[0]
        substance = substances[-1]
        rezultat = tuuls * substance
        if rezultat in challenges:
            challenges.remove(rezultat)
            tools.remove(tuuls)
            substances.pop()
        else:
            tools.append(tools.pop(0) + 1)
            substances[-1] -= 1
            if substances[-1] == 0:
                substances.pop()
    if challenges:
        print("Harry is lost in the temple. Oblivion awaits him.")
    else:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
    if tools:
        print("Tools:", ', '.join(map(str, tools)))
    if substances:
        print("Substances:", ', '.join(map(str, substances)))
    if challenges:
        print("Challenges:", ', '.join(map(str, challenges)))


tools = list(map(int, input().split()))
substances = list(map(int, input().split()))
challenges = list(map(int, input().split()))
solve_challenge(tools, substances, challenges)