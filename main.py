from ncard import NCard
import os


def playing():
    play_again = True
    while play_again:
        game_mode = input("What game would you like to play? MANGO/PINEAPPLE \n").lower()
        boards = int(input("How many boards?"))
        player_count = int(input("How many players?"))
        name_array = input("Names?").split()
        os.system('cls')
        if game_mode == "pineapple":
            NCard(3, boards, player_count, name_array)
        if game_mode == "mango":
            NCard(5, boards, player_count, name_array)
        again = input("Would you play again? y/n \n").lower()
        if again == "n":
            play_again = False


playing()
