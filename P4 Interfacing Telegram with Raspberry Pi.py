import datetime
import telepot
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO
from time import sleep
red_led_pin = 21
green_led_pin = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_led_pin, GPIO.OUT)
GPIO.setup(green_led_pin, GPIO.OUT)
now = datetime.datetime.now()
def handle(msg):
 chat_id = msg['chat']['id']
 command = msg['text']
 print ('Received:')
 print(command)
 if command == '/hi':
 bot.sendMessage (chat_id, str("Hi! "))
 elif command == '/r1':
 bot.sendMessage(chat_id, str("Red
led is ON"))
GPIO.output(red_led_pin, True)
 elif command == '/r0':
 bot.sendMessage(chat_id, str("Red
led is OFF"))
 GPIO.output(red_led_pin, False)
 elif command == '/g1':
 bot.sendMessage(chat_id,
 str("Green led is ON"))
 GPIO.output(green_led_pin, True)
 elif command == '/g0':
 bot.sendMessage(chat_id,
 str("Green led is OFF"))
 GPIO.output(green_led_pin, False)
bot =
telepot.Bot('6558187738:AAHvdvVes5nf
G2RyLWgm7zZrzTU87DzqYiY')
print (bot.getMe())
MessageLoop(bot,
handle).run_as_thread()
print ('Listening....')
while 1:
 sleep(10) 
