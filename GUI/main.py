# main.py

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
kivy.require("1.11.1")

import buzzermodule
import servomodule
import sonar_motor_module 
from screenmodule import *

class CarGridLayout(GridLayout):
    
    def servo_left(self, control):
        if control:
            try:
                servomodule.servo_left_turn()
            except Exception:
                print("Error")
                
    def servo_right(self, control):
        if control:
            try:
                servomodule.servo_right_turn()
            except Exception:
                print("Error")
                
    def servo_centre(self, control):
        if control:
            try:
                servomodule.servo_centre()
            except Exception:
                print("Error")
    
    def servo_up(self,control):
        if control:
            try:
                servomodule.servo_up()
            except Exception:
                print("Error")
    
    def servo_down(self, control):
        if control:
            try:
                servomodule.servo_down()
            except Exception:
                print("Error")
    
    def text_screen(self, text):
        if text:
            try:
                a = self.display.text
                setText('{}'.format(a))
                setRGB(200,45,11)
            except Exception:
                print("Error")
    
    def temp(self, measure):
        if measure:
            try:
                setText('temp = %02d C'%(temp))
                setRGB(200,45,11)
                self.display.text = 'Ambient temperature is {} C'.format(temp)
            except Exception:
                print("Error")
            
    def beep_on(self, beep):
        if beep:
            try:
                buzzermodule.beep_on()
            except Exception:
                print("Error")
                
    def beep_off(self, beep):
        if beep:
            try:
                buzzermodule.beep_off()
            except Exception:
                print("Error")
    
    def forward(self, forward):
        if forward:
            try:
                sonar_motor_module.forward()
            except Exception:
                print("Error") 
    
    def backward(self, backward):
        if backward:
            try:
                sonar_motor_module.backward()
            except Exception:
                print("Error")
    
    def left_turn(self, turn):
        if turn:
            try:
                sonar_motor_module.turn_left()
            except Exception:
                print("Error")
                
    def right_turn(self, turn):
        if turn:
            try:
                sonar_motor_module.turn_right()
            except Exception:
                print("Error")
                
    def stop(self, stop):
        if stop:
            try:
                sonar_motor_module.stop()
            except Exception:
                print("Error")
        
class MyCarApp(App):
    def build(self):
        return CarGridLayout()
    
carApp = MyCarApp()
carApp.run()
