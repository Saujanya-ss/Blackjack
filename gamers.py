class Gamers:
    def __init__(self, first, last, coins, loss):
        self.first = first
        self.last = last
        self.coins = coins
        self.loss = loss

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
