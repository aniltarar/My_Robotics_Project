# servomodule.py

import RPi.GPIO as GPIO
import time

def servo_down():
    servoPIN_1 = 18
    servoPIN_2 = 4

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN_1, GPIO.OUT)
    GPIO.setup(servoPIN_2, GPIO.OUT)

    p_1 = GPIO.PWM(servoPIN_1, 50) # GPIO 18 for PWM with 50Hz
    p_1.start(6) #Initialisation
    p_2 = GPIO.PWM(servoPIN_2, 50)
    p_2.start(5)

    p_1.ChangeDutyCycle(0)
    p_2.ChangeDutyCycle(0)
        
    if True:
        
        p_2.ChangeDutyCycle(8)
        time.sleep(0.5)
        p_1.ChangeDutyCycle(0)
        p_2.ChangeDutyCycle(0)
    

        
        
def servo_up():
    
    servoPIN_1 = 18
    servoPIN_2 = 4

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN_1, GPIO.OUT)
    GPIO.setup(servoPIN_2, GPIO.OUT)

    p_1 = GPIO.PWM(servoPIN_1, 50) # GPIO 18 for PWM with 50Hz
    p_1.start(6) #Initialisation
    p_2 = GPIO.PWM(servoPIN_2, 50)
    p_2.start(5)

    p_1.ChangeDutyCycle(0)
    p_2.ChangeDutyCycle(0)
    
    if True:
        
        p_2.ChangeDutyCycle(3.5)
        time.sleep(0.5)
        p_1.ChangeDutyCycle(0)
        p_2.ChangeDutyCycle(0)
    



def servo_centre():
    servoPIN_1 = 18
    servoPIN_2 = 4

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN_1, GPIO.OUT)
    GPIO.setup(servoPIN_2, GPIO.OUT)

    p_1 = GPIO.PWM(servoPIN_1, 50) # GPIO 18 for PWM with 50Hz
    p_1.start(6) #Initialisation
    p_2 = GPIO.PWM(servoPIN_2, 50)
    p_2.start(5)

    p_1.ChangeDutyCycle(0)
    p_2.ChangeDutyCycle(0)
    
    if True:
        
        p_1.ChangeDutyCycle(6)
        p_2.ChangeDutyCycle(5)
        time.sleep(0.5)
        p_1.ChangeDutyCycle(0)
        p_2.ChangeDutyCycle(0)
    


def servo_right_turn():
    servoPIN_1 = 18
    servoPIN_2 = 4

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN_1, GPIO.OUT)
    GPIO.setup(servoPIN_2, GPIO.OUT)

    p_1 = GPIO.PWM(servoPIN_1, 50) # GPIO 18 for PWM with 50Hz
    p_1.start(6) #Initialisation
    p_2 = GPIO.PWM(servoPIN_2, 50)
    p_2.start(5)

    p_1.ChangeDutyCycle(0)
    p_2.ChangeDutyCycle(0)
            
    if True:

        p_1.ChangeDutyCycle(2)
        time.sleep(0.5)
        p_1.ChangeDutyCycle(0)
        p_2.ChangeDutyCycle(0)
    


def servo_left_turn():
    servoPIN_1 = 18
    servoPIN_2 = 4

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN_1, GPIO.OUT)
    GPIO.setup(servoPIN_2, GPIO.OUT)

    p_1 = GPIO.PWM(servoPIN_1, 50) # GPIO 18 for PWM with 50Hz
    p_1.start(6) #Initialisation
    p_2 = GPIO.PWM(servoPIN_2, 50)
    p_2.start(5)

    p_1.ChangeDutyCycle(0)
    p_2.ChangeDutyCycle(0)
    
    if True:

        p_1.ChangeDutyCycle(10)
        time.sleep(0.5)
        p_1.ChangeDutyCycle(0)
        p_2.ChangeDutyCycle(0)
