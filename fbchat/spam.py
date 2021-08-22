from spambot import *

account_l = ["boxofvoodoo@gmail.com",'minarik53@seznam.cz']
account_p = ['abcde123','jachodimnagympl53']

a = 1

bot1 = SpamBot(account_l[a],account_p[a])
sleep(.1)
bot1.set_thread('Káťa Stojanová')

def spam(bot):

    while 1:
        sleep(.1)

        while 1:
            sleep(.5)
            try:
                count = bot.question('Type positive integer: ')
                if count in['break','quit','exit']:
                    return 0
                count = int(count)
                if count > 0:
                    break
            except:
                pass
            bot.send_msg('Only integers greater than 0!!')

        for i in range(count):
            bot.send_msg('spam')
            sleep(.2)
        sleep(.5)
        for i in range(count,0,-1):
            bot.send_msg(str(i))
            sleep(1)
        bot.send_msg('BOOOMM!!!!')
    
        x=bot.new_msg()

        if x in ['break','quit','exit']:
            return 0
        bot.send_msg('SpamBot will start again :P')





bot1.send_msg('Welcome to SpamBot 1.0')
spam(bot1)

bot1.send_msg('You are leaving SpamBot 1.0 :D')
