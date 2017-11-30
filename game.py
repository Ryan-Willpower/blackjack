from deal_out import DealOut
from random import randint


class Game(DealOut):
    # This is for make class usable
    def __init__(self):
        super().__init__()
        self.draw = DealOut()
        self.blackjack = 'blackjack'
        self.lose = 'lose'
        self.win = 'win'

    # draw card
    def drawcard(self, number, card):
        newnum = self.draw.randpoint()
        n = randint(0, 3)
        newsymbol = self.symbol[n]
        newcard = newnum + newsymbol
        number.append(newnum)
        card.append(newcard)

    # calculating a score
    def score(self, number):
        if self.check_blackjack(number):
            return self.blackjack
        score = 0
        a_counter = 0
        for n in number:
            if n == 'A':
                a_counter += 1
                continue
            elif n == 'J' or n == 'Q' or n == 'K':
                n = '10'
            score += int(n)
        if 'A' in number:
            score += (10 * 2)
            if score > 21:
                score -= (9 * 2)
        return score

    # if player had 2 cards
    def check_blackjack(self, player):
        if 'A' in player and len(player) == 2:
            if 'J' in player or 'Q' in player or 'K' in player:
                return self.blackjack

    # if player had more than 2 cards
    def check_score(self, score):
        if score > 21:
            return self.lose