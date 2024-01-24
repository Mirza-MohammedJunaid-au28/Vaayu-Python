from gpiozero import Servo
from time import sleep
import RPi.GPIO as gpio

# Set Servo Pin
servo1 = Servo(25)
servo2 = Servo(26)
gpio.setwarnings(False)

def move_servos(deg1,deg2):
    servo1.value = deg1
    servo2.value = deg2