from twython import TwythonStreamer
import twitterKeys as tk
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)


def blink():
    GPIO.output(13,True)
    time.sleep(1)
    GPIO.output(13,False)

class myStreamer(TwythonStreamer):
    def on_success(self,data):
        if 'text' in data:
            blink()

ck,cs,at,ats=tk.keys()

print(ck,cs,at,ats)

stream=myStreamer(ck,cs,at,ats)

stream.statuses.filter(track='Hunt_IoT')
