import random 

while True:

    selections = ["ROCK", "PAPER", "SCISSOR"]

    user_selection = input("(ENTER ALL INPUTS IN CAPS)\nCHOOSE FROM THE FOLLOWING: (ROCK , PAPER, SCISSOR): ")

    com_selection = random.choice(selections)

    print("YOU CHOSE "+ user_selection+" COMPUTER CHOSE "+com_selection)

    if user_selection == com_selection:
        print("IT'S A TIE")
    elif user_selection == "ROCK":
        if com_selection == "PAPER":
            print("COMPUTER WINS!")
        else:
            print("USER WINS!")
    elif user_selection == "PAPER":
        if com_selection == "SCISSOR":
            print("COMPUTER WINS!")
        else:
            print("USER WINS!")
    elif user_selection == "SCISSOR":
        if com_selection == "ROCK":
            print("COMPUTER WINS!")
        else:
            print("USER WINS!")

    con = input("DO YOU WANT TO PLAY AGAIN? (Y/N): ")
    if con == "N":
        break



