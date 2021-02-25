i, won, los = 10, 0, 0
while True:
    import random
    random_number = random.randint(1, 3)
    s, g, w = "s", "g", "w"

    if i >= 1:
        choise = input("Snake = s, Gun = g, Water = w")

        if choise == s and random_number == 1:
            i -= 1
            print("Tie. Remained Chances = ", int(i))
        elif choise == s and random_number == 2:
            i -= 1
            los += 1
            print("Snake died by Gun. !!!..YOU..LOOSE..!!. Remained Chances = ", int(i))
        elif choise == s and random_number == 3:
            i -= 1
            won += 1
            print("Snake won by Drinking Water. !!!..YOU..WON..!!. Remained Chances = ", int(i))

        if choise == g and random_number == 1:
            i -= 1
            won += 1
            print("Snake Died by Your Gun. !!!..YOU..WON..!!. Remained Chances = ", int(i))
        elif choise == g and random_number == 2:
            i -= 1
            print("Tie. Remained Chances = ", int(i))
        elif choise == g and random_number == 3:
            i -= 1
            los += 1
            print("Gun Dissolved in water. !!!..YOU..LOOSE..!!!. Remained Chances = ", int(i))

        if choise == w and random_number == 1:
            i -= 1
            los += 1
            print("Snake Drink water.!!!..YOU..LOOSE..!!!. Remained Chances = ", int(i))
        elif choise == w and random_number == 2:
            i -= 1
            won += 1
            print("Gun Dissolved in water. !!!..YOU..WON..!!!. Remained Chances = ", int(i))
        elif choise == w and random_number == 3:
            i -= 1
            print("Tie. Remained Chances = ", int(i))

    else:
        if won > los:
            print("Total won =", int(won))
            print("Total Loose =", int(los))
            print("...!!!***  YOU ARE  A WINNER   ***!!!....")
        elif won == los:
            print("Total won =", int(won))
            print("Total Loose =", int(los))
            print("TIE...!!!  GAME OVER  !!!....")
        else:
            print("Total won =", int(won))
            print("Total Loose =", int(los))
            print("YOU LOOSE...!!!  GAME OVER  !!!....")
        break