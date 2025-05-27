contin = True
players = {}

while contin:
    player = input("Add Player: ")
    if player == "start" or player == "":
        contin = False
    else:
        players[player] = 4
        print(f"added {player}")

print("Game Beginning with players:")
for name in players:
    print(name)

input("----------")
contin = True

def view_all():
    for name, balance in players.items():
            print(f"{name}: {balance}k")

while contin:
    currentPlayer = input("View which player: ")
    if currentPlayer == "end":
        contin = False
        print("SESSION TERMINATED")
    elif currentPlayer == "all":
        view_all()
    elif currentPlayer in players:
        print(f"{currentPlayer}: {players[currentPlayer]}k")
        calc = input("Increase/Decrease balance by: ")
        if not calc == "":
            players[currentPlayer] += int(calc)
            print(f"New Balance: {players[currentPlayer]}k")
    else:
        print("404: Player not found")