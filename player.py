
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.final_score = 0
        self.score = 0

    def get_hand(self, array):
        self.cards = array

    def increase_score(self):
        self.score += 1

    def increase_final_score(self):
        self.final_score += 1

    def reset_score(self):
        self.score = 0
