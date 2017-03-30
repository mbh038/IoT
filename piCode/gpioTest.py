import RPi.GPIO as GPIO

inputPin=2
outputPin=3

GPIO.setmode(GPIO.BCM)
GPIO.setup(outputPin,GPIO.OUT)
GPIO.setup(inputPin,GPIO.IN)
GPIO.output(outputPin,True)

def gpioTest():
    while 1: 
       if GPIO.input(inputPin): 
           GPIO.output( outputPin, False) 
       else: 
        # When the button switch is not pressed, turn off the LED. 
           GPIO.output( outputPin, True)
      
    
    
if __name__ == "__main__":
    try:
        gpioTest()
    except KeyboardInterrupt:
        pass  
