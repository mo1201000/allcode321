# Importing Libraries

import RPi.Gpio as Gpio
import time
from tkinter import *
import tkinter.font

# Libraries Imported successfully

# Raspberry Pi 3 Pin Settings

#declare  the pins off frist  motors
motorA1=2
motorA2=3
motorA3=4
#declare  the pins offsecond  motors
motorB1=5
motorB2=6
motorB3=7
#declare  the pins offthrid motors
motorC1=2
motorC2=3
motorC3=4
#declare  the pins off four  motors
motorD1=2
motorD2=3
motorD3=4

#declare  the pins off fifth  motors
motorE1=2
motorE2=3
motorE3=4

#declare  the pins off Sixthly  motors
motorF1=2
motorF2=3
motorF3=4

#declare  the pins off VII  motors
motorG1=2
motorG2=3
motorG3=4

#declare  the pins off Eighth  motors
motorZ1=2
motorZ2=3
motorZ3=4
 
Gpio.setwarnings(False)
Gpio.setmode(GPIO.BOARD) # We are accessing GPIOs according to their physical location

Gpio.setup(motorA1,Gpio.OUT)
Gpio.setup(motorA2,Gpio.OUT)
Gpio.setup(motorA3,Gpio.OUT)

Gpio.setup(motorB1,Gpio.OUT)
Gpio.setup(motorB1,Gpio.OUT)
Gpio.setup(motorB1,Gpio.OUT)


Gpio.setup(motorC1,Gpio.OUT)
Gpio.setup(motorC1,Gpio.OUT)
Gpio.setup(motorC1,Gpio.OUT)

Gpio.setup(motorD1,Gpio.OUT)
Gpio.setup(motorD1,Gpio.OUT)
Gpio.setup(motorD1,Gpio.OUT)

Gpio.setup(motorE1,Gpio.OUT)
Gpio.setup(motorE2,Gpio.OUT)
Gpio.setup(motorE3,Gpio.OUT)

Gpio.setup(motorF1,Gpio.OUT)
Gpio.setup(motorF2,Gpio.OUT)
Gpio.setup(motorF3,Gpio.OUT)

Gpio.setup(motorG1,Gpio.OUT)
Gpio.setup(motorG2,Gpio.OUT)
Gpio.setup(motorG3,Gpio.OUT)

Gpio.setup(motorZ1,Gpio.OUT)
Gpio.setup(motorZ2,Gpio.OUT)
Gpio.setup(motorZ3,Gpio.OUT)

#set the pwm pins
R1=Gpio.PWM(motorA3,300)# We have set our PWM frequency to 2000.
R1.start(100)# That's the maximum value 100 %.
R2=Gpio.PWM(motorB3,300)
R2.start(100)
R3=Gpio.PWM(motorC3,300)
R3.start(100)
R4=Gpio.PWM(motorD3,300)
R4.start(100)
R5=Gpio.PWM(motorE3,300)
R5.start(100)
R6=Gpio.PWM(motorF3,300)
R6.start(100)
R7=Gpio.PWM(motorG3,300)
R7.start(100)
R8=Gpio.PWM(motorZ3,300)
R8.start(100)




# tkinter GUI basic settings

Gui = Tk()
Gui.title("DC Motor Control with Pi 3")
Gui.config(background= "#0080FF")
Gui.minsize(800,300)
Font1 = tkinter.font.Font(family = 'Helvetica', size = 18, weight = 'bold')

# tkinter simple GUI created

def MotorForward():
    
    Gpio.setup(motorA1,Gpio.LOW)
    Gpio.setup(motorA2,Gpio.HIGH)
    Gpio.setup(motorA3,Gpio.HIGH)
                       
    Gpio.setup(motorB1,Gpio.LOW)
    Gpio.setup(motorB2,Gpio.HIGH)
    Gpio.setup(motorB3,Gpio.HIGH)
   
    Gpio.setup(motorC1,Gpio.LOW)
    Gpio.setup(motorC2,Gpio.HIGH)
    Gpio.setup(motorC3,Gpio.OUT)
 
    Gpio.setup(motorD1,Gpio.LOW)
    Gpio.setup(motorD2,Gpio.HIGH)
    Gpio.setup(motorD3,Gpio.HIGH)
    
def Motorreverse():
    Gpio.output(motorA1, Gpio.HIGH) # Motor will move in anti-clockwise direction.
    Gpio.output(motorA2, Gpio.LOW)

def MotorStop():

    Gpio.setup(motorA1,Gpio.LOW)
    Gpio.setup(motorA2,Gpio.LOW)
    Gpio.setup(motorA3,Gpio.LOW)
                       
    Gpio.setup(motorB1,Gpio.LOW)
    Gpio.setup(motorB2,Gpio.LOW)
    Gpio.setup(motorB3,Gpio.LOW)
   
    Gpio.setup(motorC1,Gpio.LOW)
    Gpio.setup(motorC2,Gpio.LOW)
    Gpio.setup(motorC3,Gpio.LOW)
 
    Gpio.setup(motorD1,Gpio.LOW)
    Gpio.setup(motorD2,Gpio.LOW)
    Gpio.setup(motorD3,Gpio.LOW)# Motor will stop.
    
    
def ChangePWM(self):
    PwmValue.ChangeDutyCycle(Scale1.get())

Text1 = Label(Gui,text='Motor Status:', font = Font1, fg='#FFFFFF', bg = '#0080FF', padx = 50, pady = 50)
Text1.grid(row=0,column=0)

Text2 = Label(Gui,text='Stop', font = Font1, fg='#FFFFFF', bg = '#0080FF', padx = 0)
Text2.grid(row=0,column=1)

Text1 = Label(Gui,text=' ', font = Font1, fg='#FFFFFF', bg = '#0080FF', padx = 150, pady = 50)
Text1.grid(row=0,column=2)

Button1 = Button(Gui, text='Clockwise', font = Font1, command = MotorForward, bg='bisque2', height = 1, width = 10)
Button1.grid(row=1,column=0)

Button2 = Button(Gui, text=' Motor Stop', font = Font1, command = MotorStop, bg='bisque2', height = 1, width = 10)
Button2.grid(row=1,column=1)

Button2 = Button(Gui, text='AntiClockwise', font = Font1, command = Motor, bg='bisque2', padx = 50, height = 1, width = 10)
Button2.grid(row=1,column=2)

Text3 = Label(Gui,text='www.TheEngineeringProjects.com', font = Font1, bg = '#0080FF', fg='#FFFFFF', padx = 50, pady = 50)
Text3.grid(row=2,columnspan=2)

Scale1 = Scale(Gui, from_=0, to=100, orient = HORIZONTAL, resolution = 1, command = ChangePWM)
Scale1.grid(row=2,column=2)

Gui.mainloop()