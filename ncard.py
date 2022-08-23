from deck import Deck
from pokereval.hand_evaluator import HandEvaluator
from discardcard import *
from player import Player
import os


class NCard:
    def __init__(self, n, boards, players, name_array):
        self.n = n
        self.boards = boards
        self.players = players
        self.name_array = name_array
        self.playncard()

    def playncard(self):
        new_deck = Deck()
        players = []
        for playerIndex in range(self.players):
            player = Player(self.name_array[playerIndex])
            player.get_hand(new_deck.dealcards(self.n))
            players.append(player)
        allboards = []
        for i in range(self.boards):
            allboards.append(new_deck.dealcards(5))

        if self.n == 5:
            i = 3
        elif self.n == 4:
            i = 4
        elif self.n == 3:
            i = 5
        for variable in range(self.n, 2, -1):
            #
            for playerIndex in range(self.players):
                discardcard(variable, players[playerIndex].cards, players[playerIndex].name)
                print(f"{players[playerIndex].name}, your hand is {players[playerIndex].cards}")
                os.system('cls')
            for j in range(self.boards):
                print(allboards[j][0: i])
            i += 1

        scores = []
        for boardIndex in range(self.boards):
            for playerIndex in range(self.players):
                scores.append(HandEvaluator.evaluate_hand(players[playerIndex].cards, allboards[boardIndex]))
            for scoreIndex in range(len(scores)):
                if max(scores) == scores[scoreIndex]:
                    players[scoreIndex].increase_score()
            scores = []

        finalPlayerScore = []
        for playerIndex in range(self.players):
            finalPlayerScore.append(players[playerIndex].score)
        for scoreIndex in range(len(finalPlayerScore)):
            if max(finalPlayerScore) == finalPlayerScore[scoreIndex]:
                players[scoreIndex].increase_final_score()
        print("Board Scores")
        board_scores = []
        for playerIndex in range(self.players):
            print(f"{players[playerIndex].name} - {players[playerIndex].score}")
            board_scores.append(players[playerIndex].score)
        if len(set(board_scores)) == 1:
            print("Tie!")
        else:
            for playerIndex in range(self.players):
                if max(board_scores) == players[playerIndex].score:
                    print(f"Congrats you won {players[playerIndex].name}")

        for playerIndex in range(self.players):
            players[playerIndex].reset_score()
            print("Current Scores\n")
            print(f"{players[playerIndex].name} - {players[playerIndex].final_score}")

