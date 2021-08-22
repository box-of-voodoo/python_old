from equation import *
from fbchat import log, Client
from fbchat.models import *
from time import sleep
from getpass import getpass

main_thread_id = "100006542950114" #100007666384414 - moje nevyhládá to tebe samotného :(
#stefan+calba - 1486566318263455 - 
#main_thread_type = ThreadType.USER
main_thread_type = ThreadType.GROUP
class SpamBot(Client):
    
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)


        if thread_id == main_thread_id:
            self.listening = False
            self.message_object = message_object
            
    def question(self,message):
        self.send_msg(message)
        return self.new_msg()
    def send_msg(self,message,emoji_size=None):
        if emoji_size:
            self.send(Message(text=message,emoji_size=emoji_size),
                      thread_id=main_thread_id, thread_type=main_thread_type)
        else:
            self.send(Message(text=message), thread_id=main_thread_id,
                      thread_type=main_thread_type)
 

    def new_msg(self):
        self.listen()
        return(self.message_object.text)

    def set_thread(self,name):
        thread = self.searchForThreads(name)[0]
        global main_thread_id
        main_thread_id = thread.uid
        global main_thread_type
        main_thread_type = thread.type

account_l = ["boxofvoodoo@gmail.com",'minarik53@seznam.cz']
account_p = ['abcde123','jachodimnagympl53']

a = 1

bot1 = SpamBot(account_l[a],account_p[a])
sleep(.1)
bot1.set_thread('Káťa Stojanová')

def calc(bot):
    x=bot.new_msg()
    if x[0] == '=':
        try:
            result = play(x[1:])
            bot.send_msg(result)
        except:
            bot.send_msg('Error')
    elif x in ['exit','quit','stop']:
        bot.logout()
        quit()
while 1:
    calc(bot1)
