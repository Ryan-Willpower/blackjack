from random import randint


class DealOut:
    def __init__(self):
        self.symbol = ('\u2660', '\u2663', '\u2665', '\u2666')
    # random some number of card
    def randpoint(self):
        numbers = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
        n = randint(0, 12)
        return numbers[n]

    # draw 2 cards to hand
    def __first_draw(self):
        hand = list()
        for n in range(2):
            hand.append(self.randpoint())
        return hand

    # for great output card style
    def shown_card(self):
        number = self.__first_draw()
        cards = list()
        for m in range(2):
            n = randint(0, 3)
            card = self.symbol[n] + number[m]
            cards.append(card)
        return [cards, number]