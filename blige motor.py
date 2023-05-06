import Rpi.Gpio as Gpio
from time import sleep

#setup the gpio pins
Gpio.setmode(Gpio.borad)
#Gpio.setmode(Gpio.BCM)
Gpio.setwarnings(False)

motorA1=2
motorA2=3

motorB1=5
motorB2=6
speed=80

#set the pins as output
Gpio.setup(motorA1,Gpio.OUT)
Gpio.setup(motorA2,Gpio.OUT)


Gpio.setup(motorB1,Gpio.OUT)
Gpio.setup(motorB1,Gpio.OUT)


while True :
    Gpio.output(motorA1,Gpio.LOW)
    Gpio.output(motorB1,Gpio.LOW)
    for  i in range(0,180,1):
        Gpio.output(motorA2,i)
        Gpio.output(motorB2,i)
    sleep(.2)

    for  i in range(180,0,-1):
        Gpio.output(motorA2,i)
        Gpio.output(motorB2,i)
    sleep(.2)
    

    Gpio.output(motorA2,Gpio.LOW)
    Gpio.output(motorB2,Gpio.LOW)
    for  i in range(0,180,1):
        Gpio.output(motorA1,i)
        Gpio.output(motorB1,i)
    sleep(.2)

    for  i in range(180,0,-1):
        Gpio.output(motorA1,i)
        Gpio.output(motorB1,i)
    sleep(.2)

    Gpio.output(motorA1,Gpio.LOW)
    Gpio.output(motorB2,Gpio.LOW)
    Gpio.output(motorA2,speed)
    Gpio.output(motorB2,speed)
    sleep(.2)

    Gpio.output(motorA2,Gpio.LOW)
    Gpio.output(motorB1,Gpio.LOW)
    Gpio.output(motorA1,speed)
    Gpio.output(motorB1,speed)
    sleep(.2)

    
    Gpio.output(motorA1,Gpio.LOW)
    Gpio.output(motorB2,Gpio.LOW)
    Gpio.output(motorA2,speed)
    Gpio.output(motorB1,speed)
    sleep(.2)

    Gpio.output(motorA2,Gpio.LOW)
    Gpio.output(motorB1,Gpio.LOW)
    Gpio.output(motorA1,speed)
    Gpio.output(motorB2,speed)
    sleep(.2)




    Gpio.output(motorA1,0)
    Gpio.output(motorB2,0)
    Gpio.output(motorA1,0)
    Gpio.output(motorB2,0)

Gpio.cleanup()

    


