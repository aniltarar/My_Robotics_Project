# buzzermodule.py

import time
import grovepi

# Connect the Grove Buzzer to digital port D8
# SIG,NC,VCC,GND
buzzer = 8

grovepi.pinMode(buzzer,"OUTPUT")

def beep_on():
    grovepi.digitalWrite(buzzer,1)
    
def beep_off():
    grovepi.digitalWrite(buzzer,0)
    
    
# while True:
#     try:
#         # Buzz for 1 second
#         grovepi.digitalWrite(buzzer,1)
#         print ('start')
#         time.sleep(1)
# 
#         # Stop buzzing for 1 second and repeat
#         grovepi.digitalWrite(buzzer,0)
#         print ('stop')
#         time.sleep(1)
# 
#     except KeyboardInterrupt:
#         grovepi.digitalWrite(buzzer,0)
#         break
#     except IOError:
#         print ("Error")
