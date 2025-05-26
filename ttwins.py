contin = True
money = 4

while contin:
    print(f"Money: {money}")
    calc = input("Change amount:")
    if calc == "end":
        print("Session Terminated")
        contin = False
    else:
        money += int(calc)