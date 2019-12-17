import RPi.GPIO as GPIO

chanel = 23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(chanel,GPIO.OUT)

GPIO.output(chanel,True)
GPIO.output(chanel,False)
