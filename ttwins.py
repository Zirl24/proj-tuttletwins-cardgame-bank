contin = True
money = {}

while contin:
    player = input("Add Player: ")
    if player == "start":
        contin = False
    else:
        money[player] = 4
        print(f"added {player}")

contin = True