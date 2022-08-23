import random
from pokereval.card import Card


class Deck:
    def __init__(self):
        self.currentDeck = self.makedeck()

    def makedeck(self):
        new_deck = []
        for cards in range(2, 15):
            cards = Card(cards, 1)
            new_deck.append(cards)
        for cards in range(2, 15):
            cards = Card(cards, 2)
            new_deck.append(cards)
        for cards in range(2, 15):
            cards = Card(cards, 3)
            new_deck.append(cards)
        for cards in range(2, 15):
            cards = Card(cards, 4)
            new_deck.append(cards)
        return new_deck

    def dealcards(self, number):
        gamecards = random.sample(self.currentDeck, number)
        for num in range(len(gamecards)):
            self.currentDeck.remove(gamecards[num])
        return gamecards