from deck import Deck
from pokereval.hand_evaluator import HandEvaluator
from pokereval.card import Card
from discardcard import *


class ThreeCard:
    def __init__(self):
        self.playthreecard()

    def playthreecard(self):
        new_deck = Deck()
        #gamecards = new_deck.dealcards(11) # ThreeCard(3) 1 = 11, 2 = 16 3 = 21
        player1 = new_deck.dealcards(3) #gamecards[0:3]
        player2 = new_deck.dealcards(3) #gamecards[3:6]
        flop = new_deck.dealcards(3)#gamecards[6:9]
        turn = new_deck.dealcards(1) #gamecards[9]
        river = new_deck.dealcards(1) #gamecards[10]
        board = flop + turn + river

        discardcard(3, player1, 1)
        discardcard(3, player2, 2)
        print(f"Player1, your hand is {player1}")
        print(f"Player2, your hand is {player2}")
        # discard = input(f"Player 1, you have {player1}, which would you like to discard? FIRST/SECOND/THIRD?").lower()
        # if discard == "first":
        #     player1.pop(0)
        # elif discard == "second":
        #     player1.pop(1)
        # elif discard == "third":
        #     player1.pop(2)
        # else:
        #     print("invalid statement")

        # discard = input(f"Player 2, you have {player2}, which would you like to discard? FIRST/SECOND/THIRD?").lower()
        # if discard == "first":
        #     player2.pop(0)
        # elif discard == "second":
        #     player2.pop(1)
        # elif discard == "third":
        #     player2.pop(2)
        # else:
        #     print("invalid statement")
        print(flop)
        print(flop, turn)
        print(board)

        score1 = HandEvaluator.evaluate_hand(player1, board)
        score2 = HandEvaluator.evaluate_hand(player2, board)

        if score1 < score2:
            print("You win player2!")
        elif score2 < score1:
            print("You win player1!")
        else:
            print("You tied!")