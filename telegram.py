# terminal command : sudo pip3 install telepot 

import datetime
import telepot
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO
from time import sleep
red_led = 7
green_led = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)
now = datetime.datetime.now()
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('Received:')
    print(command)
if command == '/hi':
    bot.sendMessage (chat_id, str("Hi! "))
elif command == '/r1':
    bot.sendMessage(chat_id, str("Red led is ON"))
    GPIO.output(red_led, True)
elif command == '/r0':
    bot.sendMessage(chat_id, str("Red led is OFF"))
    GPIO.output(red_led, False)
elif command == '/g1':
    bot.sendMessage(chat_id, str("Green led is ON"))
    GPIO.output(green_led, True)
elif command == '/g0':
    bot.sendMessage(chat_id, str("Green led is OFF"))
    GPIO.output(green_led, False)
    bot = telepot.Bot('')
    print (bot.getMe())
    MessageLoop(bot,handle).run_as_thread()
    print ('Listening....')
while 1:
    sleep(10) 
