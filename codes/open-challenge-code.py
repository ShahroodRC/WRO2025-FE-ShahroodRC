#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_2,INPUT_4,INPUT_3
from ev3dev2.sensor import Sensor, INPUT_1
from ev3dev2.sensor.lego import UltrasonicSensor,ColorSensor
from ev3dev2.motor import MediumMotor, OUTPUT_B, OUTPUT_D, SpeedPercent
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


target = 45


a=0
g=0
cr1=color_sensor.color
while cr1 != 2 and cr1 != 5: 
    cr1=color_sensor.color
    motor_b.on(60)
while g != 60:
    motor_b.on(30)
    r=rast.distance_centimeters
    c=chap.distance_centimeters
    fr=(-2*(math.sqrt(11*(r))))+100
    fc=(-2*(math.sqrt(11*(c))))+100
    target=(fc*1.3)-(fr*1.7)
    print(target)
    amotor(clamp(target,-50,50))
    g=g+1
while True:
    if cr1==2 :
        while True:
            cr1=color_sensor.color
            if  cr1 == 2:
                while cr1==2:
                    cr1=color_sensor.color
                    motor_b.on_for_degrees(80, 70)
                    motor_a.stop(stop_action='coast')
                    motor_b.stop(stop_action='coast')



                a=a+1





            motor_b.on(60)
            distance = chap.distance_centimeters
            diff =((distance-27)*-2)
            diff=diff-motor_a.position  
            diff = clamp(diff ,-32,32)
            #motor_a.on(diff)
            amotor(diff)
            



            if a==11:
                i=0
                while i!=130:
                    motor_b.on(50)
                    distance = chap.distance_centimeters
                    diff =(distance-27)*-2
                    diff=diff-motor_a.position  
                    diff = clamp(diff ,-27,27)
                    amotor(diff)
                    i=i+1
                
                break
    elif cr1 ==  5 :  
        while True:
            cr1=color_sensor.color

            if cr1 == 5:
                while cr1==5:
                    cr1=color_sensor.color
                    motor_b.on_for_degrees(80, 70)
                    motor_a.stop(stop_action='coast')
                    motor_b.stop(stop_action='coast')
                    
                a=a+1





            motor_b.on(60)
            distance = rast.distance_centimeters
            diff =(distance-27)*2
            diff=diff-motor_a.position  
            diff = clamp(diff ,-32,32)
            amotor(diff)
            if a==11:  
                i=0
                while i!=130:
                    motor_b.on(50)
                    distance = rast.distance_centimeters
                    diff =(distance-27)*2
                    diff=diff-motor_a.position  
                    diff = clamp(diff ,-27,27)
                    amotor(diff)
                    i=i+1
                        
                break

    
            


            
    motor_b.off() 
    motor_a.off()
