import Rpi.Gpio as Gpio
from time import sleep

#setup the gpio pins
Gpio.setmode(Gpio.borad)
#Gpio.setmode(Gpio.BCM)
Gpio.setwarnings(False)


#declare  the pins  motor
motorA1=2
motorA2=3

#set the pins as output
Gpio.setup(motorA1,Gpio.OUT)
Gpio.setup(motorA2,Gpio.OUT)
#set the pwm pins
# We have set our PWM frequency to 500.
R1=Gpio.PWM(motorA1,500)
R2=Gpio.PWM(motorA2,500)
 
while True:
#forward
    Gpio.output(motorA1,Gpio.LOW)
    for i in range(0,100,1):
        Gpio.output(motorA2,i)
        sleep(.1)
    sleep(.5)

    Gpio.output(motorA1,Gpio.LOW)
    for i in range(100,-1,-1):
        Gpio.output(motorA2,i)
        sleep(.1)
    sleep(.5)
#reverse
    Gpio.output(motorA2,Gpio.LOW)
    for i in range(0,100,1):
        Gpio.output(motorA1,.8*i)
        sleep(.1)
    sleep(.5)

    Gpio.output(motorA2,Gpio.LOW)
    for i in range(100,-1,-1):
        Gpio.output(motorA1,.8*i)
        sleep(.1)
    sleep(.5)
