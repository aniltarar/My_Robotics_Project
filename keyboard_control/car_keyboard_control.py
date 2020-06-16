import curses
import RPi.GPIO as GPIO          
from time import sleep

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

servoPIN_1 = 18
servoPIN_2 = 4

# Servo Setup
GPIO.setup(servoPIN_1, GPIO.OUT)
GPIO.setup(servoPIN_2, GPIO.OUT)

p_1 = GPIO.PWM(servoPIN_1, 50) # GPIO 18 for PWM with 50Hz
p_1.start(6) #Initialisation
p_2 = GPIO.PWM(servoPIN_2, 50)
p_2.start(5)

n_1 = 6
n_2 = 5

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)


print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run space-stop w-forward s-backward a-left d-right")
print("l-low m-medium h-high e-exit")
print("\n")    

try:
    
    while True:
        p_1.ChangeDutyCycle(0)
        p_2.ChangeDutyCycle(0)
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == ord('w'):
            print("forward")
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
            temp1=1
            p1.ChangeDutyCycle(100)
            p2.ChangeDutyCycle(100)
            sleep(0.09)
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
        elif char == ord('s'):
            print("backward")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)
            temp1=0
            p1.ChangeDutyCycle(100)
            p2.ChangeDutyCycle(100)
            sleep(0.09)
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
        elif char == ord('d'):
            print("right")
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
            temp1=1
            p1.ChangeDutyCycle(100)
            sleep(0.09)
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
        elif char == ord('a'):
            print("left")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in4,GPIO.HIGH)
            temp1=0
            p2.ChangeDutyCycle(100)
            sleep(0.09)
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
        elif char == curses.KEY_LEFT and n_1 <=10:
            n_1 = n_1+1.5
            print(n_1)
            p_1.ChangeDutyCycle(n_1)
            sleep(0.5)
            p_1.ChangeDutyCycle(0)
            p_2.ChangeDutyCycle(0)
        elif char == curses.KEY_RIGHT and n_1 >=3:
            n_1 = n_1-1.5
            print(n_1)
            p_1.ChangeDutyCycle(n_1)
            sleep(0.5)
            p_1.ChangeDutyCycle(0)
            p_2.ChangeDutyCycle(0)
        elif char == ord(' '):
            n_1 = 6
            n_2 = 5
            print(n_1, n_2, "Centred")
            p_1.ChangeDutyCycle(n_1)
            p_2.ChangeDutyCycle(n_2)
            sleep(0.5)
            p_1.ChangeDutyCycle(0)
            p_2.ChangeDutyCycle(0)
        elif char == curses.KEY_DOWN and n_2 < 8:
            n_2 = n_2 + 1.5
            print(n_2)
            p_2.ChangeDutyCycle(n_2)
            sleep(0.5)
            p_2.ChangeDutyCycle(0)
            p_1.ChangeDutyCycle(0)
        elif char == curses.KEY_UP and n_2 > 2:
            n_2 = n_2 - 1.5
            print(n_2)
            p_2.ChangeDutyCycle(n_2)
            sleep(0.5)
            p_2.ChangeDutyCycle(0)
            p_1.ChangeDutyCycle(0)
finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
