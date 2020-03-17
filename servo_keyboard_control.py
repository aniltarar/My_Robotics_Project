import RPi.GPIO as GPIO
import time
import curses

servoPIN_1 = 18
servoPIN_2 = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN_1, GPIO.OUT)
GPIO.setup(servoPIN_2, GPIO.OUT)

p_1 = GPIO.PWM(servoPIN_1, 50) # GPIO 18 for PWM with 50Hz
p_1.start(6) #Initialisation
p_2 = GPIO.PWM(servoPIN_2, 50)
p_2.start(5)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

n_1 = 6
n_2 = 5

try:
    while True:
        p_1.ChangeDutyCycle(0)
        p_2.ChangeDutyCycle(0)
        char = screen.getch()
        
        if char == curses.KEY_LEFT and n_1 <=10:
            n_1 = n_1+1.5
            print(n_1)
            p_1.ChangeDutyCycle(n_1)
            time.sleep(0.5)
            p_1.ChangeDutyCycle(0)
            p_2.ChangeDutyCycle(0)
        elif char == curses.KEY_RIGHT and n_1 >=3:
            n_1 = n_1-1.5
            print(n_1)
            p_1.ChangeDutyCycle(n_1)
            time.sleep(0.5)
            p_1.ChangeDutyCycle(0)
            p_2.ChangeDutyCycle(0)
        elif char == ord(' '):
            n_1 = 6
            n_2 = 5
            print(n_1, n_2, "Centred")
            p_1.ChangeDutyCycle(n_1)
            p_2.ChangeDutyCycle(n_2)
            time.sleep(0.5)
            p_1.ChangeDutyCycle(0)
            p_2.ChangeDutyCycle(0)
        elif char == curses.KEY_DOWN and n_2 < 8:
            n_2 = n_2 + 1.5
            print(n_2)
            p_2.ChangeDutyCycle(n_2)
            time.sleep(0.5)
            p_2.ChangeDutyCycle(0)
            p_1.ChangeDutyCycle(0)
        elif char == curses.KEY_UP and n_2 > 2:
            n_2 = n_2 - 1.5
            print(n_2)
            p_2.ChangeDutyCycle(n_2)
            time.sleep(0.5)
            p_2.ChangeDutyCycle(0)
            p_1.ChangeDutyCycle(0)

except KeyboardInterrupt:
    p_1.stop()
    p_2.stop()
    GPIO.cleanup()
    cap.release()
    cv2.destroyAllWindows()
finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()