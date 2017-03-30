from twython import Twython
from twython import TwythonStreamer
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

def keys():
    #Consumer Key (API Key)
    ck='Xh0uiwG5ao1r141p2uALJvTcU'

    #Consumer Secret (API Secret)
    cs='fWEGJfCQDnW77m25IX6HJx5cfwoYkueyOk7lBx5WqvUvUMmzG5'

    #Access Token
    at='846305455332900864-zy9DsYB9NNOIJgIciUVwIJzixbiCX4K'

    #Access Token Secret
    ats='TqqLZfTRGo38SBeXYAS3UyqPxFjkcOrr9K7qNYP1urFC5'

    return ck,cs,at,ats

def twSend(tweetText):
    ck,cs,at,ats=keys()
    api=Twython(ck,cs,at,ats)
    api.update_status(status=tweetText)

def twSearch(text):
    ck,cs,at,ats=keys()
    stream=myStreamer(ck,cs,at,ats)
    stream.statuses.filter(track=text)
