# My Robotics Project (Archived)

This project showcases an interactive robotics system with diverse control methods. Although this is an older project and technologies have since evolved, the core concepts and skills demonstrated remain relevant and the project offers valuable insights into the potential of robotics and automation.

The project repository is structured into different components, each focusing on specific functionalities:

## GUI Folder 
This section contains the code for the graphical user interface, which was developed using the Kivy library. The GUI provides an intuitive way for users to interact with the robot.

## Keyboard Control Folder
This contains two main programs, both written in Python3:

- `car_keyboard_control.py`: This script allows the robotic car to be controlled via the keyboard, using the 'curses' library to map specific actions to keyboard inputs.
- `servo_keyboard_control.py`: Similarly, this script enables a camera mounted on a pan/tilt servo to be controlled with the keyboard.

## Auto-Drive Script
The `auto-drive.py` script features a more autonomous functionality. When a physical button on the robotic car is pressed, it triggers a countdown followed by a sequenced buzzer. The car then starts to drive autonomously, stopping only when its front-mounted ultrasonic distance sensor detects an object in its path. It then uses the servo motors to check distances to the right and left. Based on these measurements, the car turns in the direction with the larger distance. In the unlikely event that both distances are equal, the car randomly selects a direction to turn.

This project demonstrates my ability to create interactive and autonomous robotics systems, combining different control methods and implementing sensory feedback for autonomous decision-making.
