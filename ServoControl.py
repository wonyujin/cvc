import RPi.GPIO as GPIO
import tkinter
from time import sleep



servoPin_H = 12
servoPin_V = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup([servoPin_H, servoPin_V], GPIO.OUT)
servo_H = GPIO.PWM(servoPin_H, 50)
servo_V = GPIO.PWM(servoPin_V, 50)
servo_H.start(0)
servo_V.start(0)

SERVO_MAX_DUTY = 12
SERVO_MIN_DUTY = 2.5
STEP = 3
InitDegree_H = 90
InitDegree_V = 90

class windows_tkinter:
        def __init__(self, window):
                self.window = window
                self.window.title("Raspberry Camera")
                self.window.config(background = "#FFFFFF")
                self.window.geometry('400x100+0+0')
                self.window.resizable(False, False)
 
                self.Horizontal_Degree = InitDegree_H
                self.Vertical_Degree = InitDegree_V

                self.duty_H = SERVO_MIN_DUTY + (self.Horizontal_Degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
                self.duty_V = SERVO_MIN_DUTY + (self.Vertical_Degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
                self.__main__()

        def setServoPos_H(self, arg1):
                self.Horizontal_Degree = self.Horizontal_Degree + arg1
                if self.Horizontal_Degree < 0:
                        self.Horizontal_Degree = 0
                if self.Horizontal_Degree > 180:
                        self.Horizontal_degree = 180

                self.duty_H = SERVO_MIN_DUTY + (self.Horizontal_Degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
                print("Horizontal Degree: {} & Vertical Degree: {}".format(self.Horizontal_Degree, self.Vertical_Degree))
                servo_H.ChangeDutyCycle(self.duty_H)
                sleep(0.2)

                servo_H.ChangeDutyCycle(0)

        def setServoPos_V(self, arg1):
                self.Vertical_Degree = self.Vertical_Degree + arg1
                if self.Vertical_Degree < 0:
                        self.Vertical_Degree = 0
                if self.Vertical_Degree > 180:
                        self.Vertical_degree = 180

                self.duty_V = SERVO_MIN_DUTY + (self.Vertical_Degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
                print("Horizontal Degree: {} & Vertical Degree: {}".format(self.Horizontal_Degree, self.Vertical_Degree))
                servo_V.ChangeDutyCycle(self.duty_V)
                sleep(0.2)

                servo_V.ChangeDutyCycle(0)
                
          


        def __main__(self):
                BTN_LEFT = tkinter.Button(self.window,command=lambda: self.setServoPos_H(STEP),overrelief="raised", width=10, text="LEFT", cursor="sb_left_arrow")
                BTN_LEFT.place(x=0,y=40,width=100,height=20)

                BTN_RIGHT = tkinter.Button(self.window,command=lambda: self.setServoPos_H(-STEP),overrelief="raised", width=10, text="RIGHT", cursor="sb_right_arrow")
                BTN_RIGHT.place(x=300,y=40,width=100,height=20)

                BTN_UP = tkinter.Button(self.window,command=lambda: self.setServoPos_V(STEP),overrelief="raised", width=10, text="UP", cursor="based_arrow_up")
                BTN_UP.place(x=150,y=10,width=100,height=20)

                BTN_DOWN = tkinter.Button(self.window,command=lambda: self.setServoPos_V(-STEP),overrelief="raised", width=10, text="DOWN", cursor="based_arrow_down")
                BTN_DOWN.place(x=150,y=70,width=100,height=20)
                
               
                

def InitServoPos():
       duty_H = SERVO_MIN_DUTY + (InitDegree_H*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
       duty_V = SERVO_MIN_DUTY + (InitDegree_V*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)

       print("Horizontal Degree: {} & Vertical Degree: {}".format(InitDegree_H, InitDegree_V))
       servo_H.ChangeDutyCycle(duty_H)
       sleep(1)
       servo_V.ChangeDutyCycle(duty_V)
       sleep(1)
       servo_H.ChangeDutyCycle(0)
       sleep(0.2)
       servo_V.ChangeDutyCycle(0)
       sleep(0.2)


if __name__ == "__main__":

        InitServoPos()
        win = tkinter.Tk()
        windows_tkinter(win)
        win.mainloop()
        servo_H.stop()
        servo_V.stop()
        GPIO.cleanup()
