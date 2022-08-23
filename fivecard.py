from deck import Deck
from pokereval.hand_evaluator import HandEvaluator
from pokereval.card import Card
from discardcard import *


class FiveCard:
    def __init__(self):
        self.playfivecard()

    def playfivecard(self):
        new_deck = Deck()
        #gamecards = new_deck.dealcards(15)
        player1 = new_deck.dealcards(5)
        player2 = new_deck.dealcards(5)
        flop = new_deck.dealcards(3)
        turn = new_deck.dealcards(1)
        river = new_deck.dealcards(1)
        board = flop + turn + river

        discardcard(5, player1, 1)
        discardcard(5, player2, 2)
        print(flop)

        discardcard(4, player1, 1)
        discardcard(4, player2, 2)
        print(flop, turn)

        discardcard(3, player1, 1)
        discardcard(3, player2, 2)
        print(board)

        score1 = HandEvaluator.evaluate_hand(player1, board)
        score2 = HandEvaluator.evaluate_hand(player2, board)

        if score1 < score2:
            print("You win player2!")
        elif score2 < score1:
            print("You win player1!")
        else:
            print("You tied!")