from pyrogram import Client
from pyrogram.raw.functions.contacts import Search
import time
import sys

def update_msg(text):
    message = f'\r{text}'
    sys.stdout.write(message)
    sys.stdout.flush()

api_id = '26158705'
api_hash = '791ecb9840feac6681198410958729a5'
phone = ''
login = 'catskin'

phone = input('Введите свой номер телефона: ')

bot = Client(name=login, api_id=api_id, api_hash=api_hash, phone_number=phone)                      
bot.start()

id_chat = input('Введите юзернейм чата (Без @): ')

while True:        
    sleepon = True
    bot.send_message(chat_id=id_chat, text='кошка скин')
    print('Sended!')
    unixtime = int(time.time())
    while sleepon:
        time.sleep(1)
        if (int(time.time()) - unixtime) > 901:
            sleepon = False
            print('\n')
        else:
            sec = int(time.time()) - unixtime
            update_msg(f"Прошло {sec} секунд")
     
bot.stop()
