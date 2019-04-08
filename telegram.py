import telepot
from pprint import pprint
import sys
import time
import datetime
import random

data = time.strftime("[%A] %d/%m/%Y - %H:%M:%S")

def handle(msg):
    resposta = bot.getUpdates()
    print(resposta)
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Comando recebido: %s' % command)

    if command == '/mamaemandou':
        rand = random.randint(1, 3)
        rand_casa_fora = random.randint(1, 2)

        if rand_casa_fora == 1:
            bot.sendMessage(chat_id, 'Time da casa: ')

        else:
            bot.sendMessage(chat_id, 'Time visitante:')

        if rand == 1:
            bot.sendMessage(chat_id, 'Vitória')

        elif rand == 2:
            bot.sendMessage(chat_id, 'Empate')

        else:
            bot.sendMessage(chat_id, 'Derrota')



    if command == '/data':
        bot.sendMessage(chat_id, str(data))

bot = telepot.Bot('879354760:AAF4JiZOadBOx4cLg3O2CstEui2SAE0h1-A')
bot.message_loop(handle)

while True:
    time.sleep(10)
