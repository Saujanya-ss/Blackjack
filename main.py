import sqlite3
from deck import Deck
from player import Player
from gamers import Gamers

conn = sqlite3.connect('userdata.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS players (
            first text,
            last text,
            coins integer
            loss integer
            )""")

conn.commit()

def insert_user(game):
    with conn:
        c.execute("INSERT INTO players VALUES (:first, :last, :coins, :loss)", {'first': game.first, 'last': game.last, 'coins': game.coins, 'loss':game.loss})


def get_user_by_name(firstname):
    c.execute("SELECT * FROM players WHERE first=:first", {'first': firstname})
    return c.fetchall()


def update_coins(game, coins):
    with conn:
        c.execute("""UPDATE players SET coins = :coins
                    WHERE first = :first AND last = :last""",
                  {'first': game.first, 'last': game.last, 'coins': coins})


def remove_emp(game):
    with conn:
        c.execute("DELETE from players WHERE first = :first AND last = :last",
                  {'first': game.first, 'last': game.last})


a = input("Enter Name : ")
gam = input("Enter Gamer tag : ")

count = {
    "win": 0,
    "lose": 0
}

game = Gamers( a, gam ,count["win"] )
insert_user(game)
val='Y'


while val.upper() == 'Y': 
    coin = coin + 1 
    class Blackjack:
        def __init__(self):
            self.deck = Deck()
            self.deck.generate()
            self.player = Player(False, self.deck)
            self.dealer = Player(True, self.deck)
                        
        def play(self):
            p_status = self.player.deal()
            d_status = self.dealer.deal()

            self.player.show()

            if p_status == 1:
                print("Player got Blackjack! Congrats!")
                if d_status == 1:
                    print("Dealer and Player got Blackjack! It's a push. (Tie)")
                return 1

            cmd = ""
            while cmd != "Stand":
                bust = 0
                cmd = input("Hit or Stand? :")

                if cmd == "Hit":
                    bust = self.player.hit()
                    self.player.show()
                if bust == 1:
                    print("Player busted. Good Game!")
                    return 1
            print("\n")
            self.dealer.show()
            if d_status == 1:
                print("Dealer got Blackjack! Better luck next time!")
                return 1

            while self.dealer.check_score() < 17:
                if self.dealer.hit() == 1:
                    self.dealer.show()
                    print("Dealer busted. Congrats!")
                    return 1
                self.dealer.show()

            if self.dealer.check_score() == self.player.check_score():
                print("It's a Push (Tie). Better luck next time!")
            elif self.dealer.check_score() > self.player.check_score():
                print("Dealer wins. Good Game!")
                count["lose"] += 1
            elif self.dealer.check_score() < self.player.check_score():
                print("Player wins. Congratulations!")  
                count["win"] += 1
                 
           
    b = Blackjack()
    b.play()

    val = input("Play one more Game: ? (Y/N)")


update_coins(game,count["win"],count["lose"])



conn.close()



