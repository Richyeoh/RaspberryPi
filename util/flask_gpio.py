from flask import Flask
import RPi.GPIO as GPIO

app=Flask(__name__)

chanel=23

def init_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(chanel,GPIO.OUT)
    
@app.route('/open')
def open():
    GPIO.output(chanel,True)
    return 'ok~'
    
@app.route('/close')
def close():
    GPIO.output(chanel,False)
    return 'ok~'
    
if __name__ == '__main__':
    init_gpio()
    app.run(host='0.0.0.0',port=8080)
