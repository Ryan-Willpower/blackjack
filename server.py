import socket
import threading
from time import sleep
from deal_out import DealOut
from game import Game
from bot import Bot

draw = DealOut()
game = Game()
bot = Bot()

s = socket.socket()
host = ''
port = 12345

def blackjack(con):
    try:
        overhand = False
        one = 'game started!!'
        con.send(one.encode())

        while True:
            player = game.shown_card()
            if player[0][0] != player[0][1]:
                while True:
                    computer = game.shown_card()
                    if computer[0][0] != computer[0][1]:
                        bot.reset_score()
                        break
                break

        player_score = game.score(player[1])

        two = ("computer: " + str(computer[0][0]) + "\nplayer: " + str(player[0]))
        con.send(two.encode())

        sleep(2)

        manu = (f"""########manu########
\nNow you have {player[0]} ({player_score})
1. draw more
2. hold
select: """)
        con.send(manu.encode())
        manu = con.recv(1024).decode()
        if manu == '1':
            game.drawcard(player[1], player[0])
            player_score = game.score(player[1])
            hand = player[0], player_score
            con.send(str(hand).encode())
            if game.check_score(player_score) == game.lose:
                overhand = True
                lose = 'you lose'
                con.send(lose.encode())
        elif manu == '2':
            hold = "You select to hold"
            con.send(hold.encode())

        if overhand == False:
            while True:
                thought = bot.thinking(computer[1], computer[0])
                print(thought)
                if thought == bot.want_more:
                    bot.bot_draw_more(computer[1], computer[0])
                    print(computer[1], bot.score)
                elif thought == bot.nah:
                    print("end bot")
                    break

            computer_hand = computer[0], bot.score

            con.send(str(computer_hand).encode())

            text = f"\nyou're now have {player_score} and bot have {bot.score}\n"
            con.send(text.encode())
            stat = 'unknown'
            if player_score <= 21 and bot.score <= 21:
                if player_score > bot.score:
                    stat = "player win!!"
                elif player_score == bot.score:
                    stat = "draw"
                elif player_score < bot.score:
                    stat = "computer win.. you're such a noob.."
                elif player_score == 'blackjack':
                    if bot.score != 'blackjack':
                        stat = "player win!!"
                    else:
                        stat = "draw"
                elif bot.score == 'blackjack':
                    if player_score != 'blackjack':
                        stat = "computer win.. you're such a noob.."
                    else:
                        stat = "draw"
            else:
                stat = "player win!!"
            con.send(stat.encode())
    except ConnectionResetError:
        pass

s.bind((host, port))
s.listen(10)

print('server is starting')
while True:
    print("wait for player..")
    con, address = s.accept()
    t = threading.Thread(target=blackjack, args=(con, )).start()