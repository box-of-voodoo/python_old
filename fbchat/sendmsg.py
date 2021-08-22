from fbchat import Client
from fbchat.models import *
from time import sleep

##login = "boxofvoodoo@gmail.com"
##password = 'abcde123'

login = 'minarik53@seznam.cz'
password = 'jachodimnagympl53'



client = Client(login,password)
print('Own id: {}'.format(client.uid))
sleep(0.5)



##users = client.searchForUsers('*')
##client.send(Message(text='Hi me!'), thread_id=client.uid, thread_type=ThreadType.USER)


##for user in users:
##    print(user)
##print()
# Fetches a list of the 10 top threads you're currently chatting with
threads = client.fetchThreadList(limit = 10)
print(threads)
# Fetches the next 10 threads
threads += client.fetchThreadList(offset=20, limit=10)
for thread in threads:
    print(thread)

print('x')

### Gets the last 10 messages sent to the thread
##messages = client.fetchThreadMessages(thread_id=client.uid, limit=1)
### Since the message come in reversed order, reverse them
##messages.reverse()
##
##print(messages)

sleep(.5)
client.logout()
input()
