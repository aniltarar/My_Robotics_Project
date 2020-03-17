import RPi.GPIO as GPIO
import grovepi
from time import sleep
import random
import math

ultrasonic_ranger = 4
buzzer = 8
button = 3
#Temp_sensor pin & type:
temp_sensor = 6
blue = 0 #The Blue colored sensor
white = 1 #The White colored sensor
#Motor Inlets
in1 = 24
in2 = 23
en1 = 25
in3 = 27
in4 = 22
en2 = 17
temp1=1

#Servo inlets
servoPIN_1 = 18
servoPIN_2 = 4
obstacle_sensor = 21

GPIO.setmode(GPIO.BCM)
#Obstacle Detector Setup:
GPIO.setup(obstacle_sensor, GPIO.IN)
GPIO.input(obstacle_sensor)
#Buzzer & Button GPIO setups:
grovepi.pinMode(buzzer,"OUTPUT")
grovepi.pinMode(button,"INPUT")

#Motor GPIO setmode
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
p1.start(90)
p2.start(90)

#Servo GPIO setup
GPIO.setup(servoPIN_1, GPIO.OUT)
GPIO.setup(servoPIN_2, GPIO.OUT)
p_1 = GPIO.PWM(servoPIN_1, 50) #GPIO 18 for PWM with 50Hz
p_1.start(6) #Initialisation Servo1
p_2 = GPIO.PWM(servoPIN_2, 50) ##GPIO 4 for PWM with 50Hz
p_2.start(5) #Initialisation Servo2
sleep(.1)
p_1.ChangeDutyCycle(0)
p_2.ChangeDutyCycle(0)


#Motor control definitions:
def forward(x):
    print("forward")
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    p1.ChangeDutyCycle(90)
    p2.ChangeDutyCycle(90)
    temp1=1
    sleep(x)
def backward(x):
    print("backward")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    p1.ChangeDutyCycle(90)
    p2.ChangeDutyCycle(90)
    temp1=0
    sleep(x)

def stop():
    print("stop")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

def turn_right(x):
    print("Turning right.")
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    temp1=1
    p1.ChangeDutyCycle(100)
    p2.ChangeDutyCycle(100)
    sleep(x)

def turn_left(x):
    print("Turning left.")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in4,GPIO.HIGH)
    temp1=1
    p1.ChangeDutyCycle(100)
    p2.ChangeDutyCycle(100)
    sleep(x)

def servo_radar_mode():
    p_1.ChangeDutyCycle(4)
    sleep(0.4)
    p_1.ChangeDutyCycle(0)
    p_2.ChangeDutyCycle(0)
    p_1.ChangeDutyCycle(6)
    sleep(0.4)
    p_1.ChangeDutyCycle(0)
    p_2.ChangeDutyCycle(0)
    p_1.ChangeDutyCycle(8)
    sleep(0.4)
    p_1.ChangeDutyCycle(0)
    p_2.ChangeDutyCycle(0)
    
#Servo motor definitions:
def servo_right():
    print("Looking right")
    p_1.ChangeDutyCycle(2)
    #print(">>>Distance<<< \n",grovepi.ultrasonicRead(ultrasonic_ranger),"CM")
    sleep(0.6)
    p_1.ChangeDutyCycle(0)
    p_2.ChangeDutyCycle(0)

def servo_left():
    print("Looking left")
    p_1.ChangeDutyCycle(11)
    #print(">>>Distance<<< \n",grovepi.ultrasonicRead(ultrasonic_ranger),"CM")
    sleep(0.6)
    p_1.ChangeDutyCycle(0)
    p_2.ChangeDutyCycle(0)

def servo_centre():
    print("Deciding...")
    p_1.ChangeDutyCycle(6)
    sleep(0.6)
    p_1.ChangeDutyCycle(0)
    p_2.ChangeDutyCycle(0)

def countdown(n):
    while n>0:
        print("Starting in ", n , "seconds.")
        n = n - 1
        sleep(1)
        if (n == 0):
            print("<<<<<<START>>>>>>")
            grovepi.digitalWrite(buzzer,1)
            sleep(0.3)
            grovepi.digitalWrite(buzzer,0)
            sleep(0.3)
            grovepi.digitalWrite(buzzer,1)
            sleep(0.3)
            grovepi.digitalWrite(buzzer,0)
            sleep(0.3)
            grovepi.digitalWrite(buzzer,1)
            sleep(0.009)
            grovepi.digitalWrite(buzzer,0)
            sleep(0.09)
            grovepi.digitalWrite(buzzer,1)
            sleep(0.009)
            grovepi.digitalWrite(buzzer,0)
            sleep(0.09)
            grovepi.digitalWrite(buzzer,1)
            sleep(0.009)
            grovepi.digitalWrite(buzzer,0)
            sleep(0.09)
            grovepi.digitalWrite(buzzer,1)
            sleep(0.009)
            grovepi.digitalWrite(buzzer,0)
            sleep(0.09)
            grovepi.digitalWrite(buzzer,1)
            sleep(0.009)
            grovepi.digitalWrite(buzzer,0)
            sleep(0.09)
            grovepi.digitalWrite(buzzer,1)
            sleep(0.009)
            grovepi.digitalWrite(buzzer,0)

def random_turn_left():
    sleep(1)
    backward(0.5)
    turn_left(0.6)
    distance_list.clear()
    
def random_turn_right():
    sleep(1)
    backward(0.5)
    turn_right(0.6)
    distance_list.clear()

[temp,humidity] = grovepi.dht(temp_sensor,blue)  
if math.isnan(temp) == False and math.isnan(humidity) == False:
    print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
print(">>>Press the button<<< \n\nAuto Drive OFF")
while (grovepi.digitalRead(button)==0):
    if (grovepi.digitalRead(button)==1):
        break

print("\n")
print("Auto Drive ON")
print("\n")
countdown(3)

try:
    while True:
        print(grovepi.ultrasonicRead(ultrasonic_ranger))
#         servo_radar_mode()
        if(grovepi.ultrasonicRead(ultrasonic_ranger) >= 30 and GPIO.input(obstacle_sensor)==1):  
            forward(0.05)
            print(grovepi.ultrasonicRead(ultrasonic_ranger),"CM\nGoing Forward")
        elif(grovepi.ultrasonicRead(ultrasonic_ranger) <= 30 or GPIO.input(obstacle_sensor)==0):    
            stop()
            sleep(1)
            backward(0.23)
            stop()
            sleep(.5)
            distance_list = []
            servo_right()
            distance_list.append(grovepi.ultrasonicRead(ultrasonic_ranger))
            print("Measured Distance ",distance_list[0], "CM.")
            sleep(1)
            servo_left()
            distance_list.append(grovepi.ultrasonicRead(ultrasonic_ranger))
            print("Measured Distance ",distance_list[1], "CM.")
            sleep(1)
            servo_centre()
            sleep(1.5)
            while (len(distance_list)==2):
                if(distance_list[0]>distance_list[1]):
                    sleep(1)
                    turn_right(.6)
                    distance_list.clear()
                elif(distance_list[0]<distance_list[1]):
                    sleep(1)
                    turn_left(.6)
                    distance_list.clear()
                elif(distance_list[0]==distance_list[1]):
                    random_turn_list = [random_turn_right(), random_turn_left()]
                    random.choice(random_turn_list)
                    distance_list.clear()
                else:
                    pass
            else:
                pass
                
except KeyboardInterrupt:
    stop()
    servo_centre()
    pass
finally:
    GPIO.cleanup()
