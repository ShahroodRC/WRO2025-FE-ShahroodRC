#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_2,INPUT_4,INPUT_3
from ev3dev2.sensor import Sensor, INPUT_1
from ev3dev2.sensor.lego import UltrasonicSensor,ColorSensor
from ev3dev2.motor import MediumMotor, OUTPUT_B, OUTPUT_D, SpeedPercent, SpeedRPS, OUTPUT_C
from time import sleep
import time
import math
from ev3dev2.button import Button
from ev3dev2.led import Leds



rast = UltrasonicSensor(INPUT_2)
chap = UltrasonicSensor(INPUT_3)
color_sensor = ColorSensor(INPUT_4)
motor_a = MediumMotor(OUTPUT_B)
motor_b = MediumMotor(OUTPUT_D)
motor_c = MediumMotor(OUTPUT_C)


motor_a.reset() 




btn = Button()
leds = Leds()
leds.set_color('LEFT', 'ORANGE')
leds.set_color('RIGHT', 'ORANGE')


btn.wait_for_bump('enter')
leds.set_color('LEFT', 'GREEN')
leds.set_color('RIGHT', 'GREEN')

minDi=math.inf

def clamp(value, minimum, maximum):
    if value > maximum : value=maximum
    if value < minimum : value=minimum
    return value


def amotor(degrese,cl=50):
        diff =degrese
        diff=diff-motor_a.position
        diff=clamp(diff,-cl,cl)  

        motor_a.on(diff)


a=0


def lineChek():
    global a

    cr1=color_sensor.color

    if (motor_b.position>1000  and  (cr1 == 1 or cr1 ==5 or cr1==2 or cr1==7)) or (a==0 and(cr1 == 1 or cr1 ==5 or cr1==2 or cr1==7 )):
        
        a=a+1
        motor_b.reset()



target = 45
abi=[1,2]
narengi=[5,7]
g=0
cr1=color_sensor.color
speed=40

while g != 120:
    if cr1 == 6 : 
        cr1=color_sensor.color
    else:
        speed=100
        

    motor_b.on(speed)
    motor_c.on(speed)

    r=rast.distance_centimeters
    c=chap.distance_centimeters
    fr=(-2*(math.sqrt(11*(r))))+100
    fc=(-2*(math.sqrt(11*(c))))+100
    target=(fc*1.3)-(fr*1.3)
    amotor(clamp(target,-28,28))
    g=g+1
while True:
    if cr1== abi[0] or cr1==abi[1]:
        while True:
            lineChek()
            motor_b.on(100)
            motor_c.on(100)
            distance = chap.distance_centimeters
            diff =(distance-28)*-2
            diff=diff-motor_a.position  
            diff = clamp(diff ,-35,35)
            amotor(diff)
            lineChek()
            if a==11:
                i=0
                while i!=60:
                    motor_b.on(100)
                    motor_c.on(100)
                    distance = chap.distance_centimeters
                    diff =(distance-28)*-2
                    diff=diff-motor_a.position  
                    diff = clamp(diff ,-35,35)
                    amotor(diff)
                    i=i+1
                
                break
        
    elif cr1== narengi[0] or cr1==narengi[1]:
        while True:
            lineChek()    
            motor_b.on(100)
            motor_c.on(100)
            distance = rast.distance_centimeters
            diff =(distance-28)*2
            diff=diff-motor_a.position  
            diff = clamp(diff ,-35,35)
            amotor(diff)
            lineChek()
            if a==11:  
                i=0
                while i!=60:
                    motor_b.on(100)
                    motor_c.on(100)
                    distance = rast.distance_centimeters
                    diff =(distance-28)*2
                    diff=diff-motor_a.position  
                    diff = clamp(diff ,-35,35)
                    amotor(diff)
                    i=i+1
                break
    break
motor_b.off() 
motor_a.off()
motor_c.off()

