from game import Game
from deal_out import DealOut


class Bot(Game, DealOut):
    def __init__(self):
        super().__init__()
        self.game = Game()
        self.score = 0
        # self.bot_stat = self.bot_first_draw()
        self.want_more = 'more'
        self.nah = 'nah'

    def reset_score(self):
        self.score = 0

    # Yeah.. Bot is thinking..
    def thinking(self, num, sym):
        if self.game.check_blackjack(num) != self.blackjack:
            if self.score < 19:
                self.score = self.game.score(num)
                return self.want_more
            else:
                return self.nah

    # Yes, He think he wanna draw more..
    def bot_draw_more(self, number, card):
        thought = self.thinking(number, card)
        if thought == self.want_more and self.score < 19:
            self.game.drawcard(number, card)
            self.score = self.game.score(number)