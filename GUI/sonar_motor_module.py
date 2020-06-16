# sonar_motor_module.py

import RPi.GPIO as GPIO          
from time import sleep
import grovepi

ultrasonic_ranger = 7

in1 = 24
in2 = 23
en1 = 25
in3 = 27
in4 = 22
en2 = 17
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p1=GPIO.PWM(en1,1000)
p2=GPIO.PWM(en2,1000)
p1.start(100)
p2.start(100)


def forward():
    if (grovepi.ultrasonicRead(ultrasonic_ranger)) >= 20:
        try:
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
            temp1=1
            
        except Exception:
            print("Error")
            
    if (grovepi.ultrasonicRead(ultrasonic_ranger)) <= 20:
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        
def backward():
    if (grovepi.ultrasonicRead(ultrasonic_ranger)) >= 2:
        try:
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)
            temp1=0
            
        except Exception:
            print("Error")
            
    if (grovepi.ultrasonicRead(ultrasonic_ranger)) <= 2:
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)

def stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)


def turn_left():
    if (grovepi.ultrasonicRead(ultrasonic_ranger)) >= 2:
        try:
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in4,GPIO.HIGH)
            temp1=0
        except Exception:
            print("Error")
            
    if (grovepi.ultrasonicRead(ultrasonic_ranger)) <= 2:
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        
def turn_right():
    if (grovepi.ultrasonicRead(ultrasonic_ranger)) >= 2:
        try:
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
            temp1=0
        except Exception:
            print("Error")
            
    if (grovepi.ultrasonicRead(ultrasonic_ranger)) <= 2:
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
