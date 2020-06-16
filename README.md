# My_Robotics_Project
Codes for my first robotics project. 

The 'car_keyboard_control.py' is the code to control the robot via the keyboard. It is written in Python3 and uses 'curses' library 
to assign tasks to keyboard keys.

Likewise 'servo_keyboard_control.py' is written in Python3 to allow controlling a camera attached pan/tilt servo with the keyboard.

Finally, 'auto-drive.py' waits for the user to press the physical button on the car that initiates a countdown followed by a 
sequenced buzzer. Then the car drives until its front mounted ultra-sonic distance sensor senses an object in front of the car. Then 
the servo motors check both right and left directions and get a measurement of the distance on each side. After that turns the car
into the direction where the measurement is bigger. If the distance on each side is the same (very less likely) the car decides 
which side to turn randomly.
