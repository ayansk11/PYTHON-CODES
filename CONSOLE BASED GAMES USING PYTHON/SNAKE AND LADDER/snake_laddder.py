import time
import random
import sys

max = 100

snakes = {

    17: 7,
    54: 34,
    62: 19,
    64: 60,
    87: 36,
    95: 75,
    93: 73,
    98: 79,

}

ladders = {
    
    4: 14,
    9: 31,
    1: 38,
    21: 42,
    28: 84,
    51: 67,
    72: 91,
    80: 99
    
}

def welcome_msg():

    msg = "~~~~ Welcome to Snake and Ladder Game ~~~~"
    print(msg)


def get_player_names():

    player1 = input("PLAYER 1: ")
    player2 = input("PLAYER 2: ")

    print(f"\nMATCH WILL BE PLAYED BETWEEN {player1} and {player2}\n")

    return player1, player2


def get_dice_value():

    time.sleep(2)
    x = random.randint(1, 6)

    print(f"IT'S A {x}\n")

    return x


def got_snake_bite(old_value, current_value, player_name):

    print("\n" + "Snake Bite" + " ~~~~~~~~>")
    print(f"\n{player_name} got a snake bite......\nDown to {current_value} from {old_value}\n")


def got_ladder_jump(old_value, current_value, player_name):

    print(f"\nFound a ladder.......\n")
    print(f"{player_name} climbed the ladder from {old_value} to {current_value}")


def snake_ladder(player_name, current_value, dice_value):

    time.sleep(2)
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > max:

        print(f"\nYou need {max - old_value} to win this game\nKeep trying.......\n")

        return old_value

    print(f"\n{player_name} moved from {old_value} to {current_value}")

    if current_value in snakes:

        final_value = snakes.get(current_value)
        got_snake_bite(current_value, final_value, player_name)
    elif current_value in ladders:

        final_value = ladders.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)
    else:
        final_value = current_value
    
    return final_value


def check_win(player_name, position):
    
    time.sleep(2)

    if max == position:
        
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        print("\nThank you for playing the game. Hope you enjoyed the game\n\n")
        sys.exit(1)
        
welcome_msg()
time.sleep(2)

player1_name, player2_name = get_player_names()
time.sleep(2)
player1_current_position = 0
player2_current_position = 0

while True:

    time.sleep(2)

    input_1 = input(f"\n{player1_name}  HIT THE ENTER TO ROLL DICE: \n")
    print("Rolling dice.....\n")

    dice_value = get_dice_value()
    time.sleep(2)

    print(f"\n{player1_name} moving....\n")

    player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)

    check_win(player1_name, player1_current_position)

    input_2 = input(f"\n{player2_name}  HIT THE ENTER TO ROLL DICE: \n")
    print("Rolling dice.....\n")

    dice_value = get_dice_value()

    time.sleep(2)
    print(f"\n{player2_name} moving....\n")

    player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)

    check_win(player2_name, player2_current_position)

